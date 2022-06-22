#!/usr/bin/env python

# General imports
import rospy

# Msg, srv and cfg imports:
from smart_python_ros_node.msg import smartCommonData

# Define some light methods and callbacks. For heavy stuff, use modules and classes.
def callback(data):
    """Handle subscriber data."""
    # Simply print out values in our custom message.
    rospy.loginfo(
        "%s: I heard %s, a + b = %d", rospy.get_name(), data.message, data.a + data.b
    )


def listener():
    """Configure subscriber."""
    # Create a subscriber with appropriate topic, custom message and name of
    # callback function.
    rospy.Subscriber("smart_topic", smartCommonData, callback)


# Main function.
if __name__ == "__main__":
    # Initialize the node and name it.
    rospy.init_node("smart_listener")
    # Go to the main loop.
    listener()
    # Wait for messages on topic, go to callback function when new messages
    # arrive.
    rospy.spin()