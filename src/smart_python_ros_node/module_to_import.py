#!/usr/bin/env python

# General imports:
import rospy

# Run a dynamic reconfigure server
from dynamic_reconfigure.server import Server as DynamicReconfigureServer

# Msg, srv and cfg imports:
from std_msgs.msg import String
from smart_python_ros_node.msg import smartCommonData
from smart_python_ros_node.cfg import smartCommonConfig as ConfigType

# Everything should be in a class structure, with at least three 
# methods: init, start, stop and reconfigure
class smartCommonClass():

    # Must have __init__(self) 
    def __init__(self):

        """Get the parameters"""
        # Get the private namespace parameters from the parameter server:
        # set from either command line or launch file. Change these parameters
        # according to your node requirements. 
        rate = rospy.get_param("~rate", 1.0)
        # Initialize enable variable so it can be used in dynamic reconfigure
        # callback upon startup.
        self.enable = True
        # Create a dynamic reconfigure server.
        self.server = DynamicReconfigureServer(ConfigType, self.reconfigure_cb)
        # Create a publisher for our custom message. Adjust according to your 
        # node requirements. 
        self.pub = rospy.Publisher("smart_topic", smartCommonData, queue_size=10)
        # Initialize message variables. Adjust according to your node requirements. 
        self.enable = rospy.get_param("~enable", True)
        self.int_a = rospy.get_param("~a", 1)
        self.int_b = rospy.get_param("~b", 2)
        self.message = rospy.get_param("~message", "hello")

        rospy.loginfo("Test node running sucessfully")

        if self.enable:
            self.start()
        else:
            self.stop()

        # Create a timer to go to a callback at a specified interval. Adjust according
        # to your node requirements. 
        rospy.Timer(rospy.Duration(1.0/rate), self.timer_cb)

    def start(self):
        """Turn on publisher"""
        self.pub = rospy.Publisher("smart_topic", smartCommonData, queue_size=10)

    def stop(self):
        """Turn off publisher"""
        self.pub.unregister()

    def timer_cb(self, _event):
        """Call at a specified interval to publish message"""
        if not self.enable:
            return

        # Set the message type to publish as our custom message.
        msg = smartCommonData()
        # Assign message fields to values from the parameter server.
        msg.message = rospy.get_param("~message", self.message)
        msg.a = rospy.get_param("~a", self.int_a)
        msg.b = rospy.get_param("~b", self.int_b)

        # Fill in custom message variables with values updated from dynamic
        # reconfigure server.
        self.message = msg.message
        self.int_a = msg.a
        self.int_b = msg.b

        # Publish our custom message.
        self.pub.publish(msg)
        
    def reconfigure_cb(self, config, dummy):
        """Create a callback function for the dynamic reconfigure server."""
        # Fill in local variables with values received from dynamic reconfigure
        # clients (typically the GUI).
        self.message = config["message"]
        self.int_a = config["a"]
        self.int_b = config["b"]

        # Check to see if node should be started or stopped.
        if self.enable != config["enable"]:
            if config["enable"]:
                self.start()
            else:
                self.stop()
        self.enable = config["enable"]

        # Return the new variables.
        return config    
