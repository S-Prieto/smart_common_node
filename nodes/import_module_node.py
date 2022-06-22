#!/usr/bin/env python

import rospy

from smart_python_ros_node.module_to_import import smartCommonClass

# Define a main function and then call it
def main():
    # Initialize node and name it
    rospy.init_node("smart_python_ros_node")
    rospy.loginfo("SMART common node")
    # Go to class functions that do all the heavy lifting
    try:
        smartCommonClass()
    except rospy.ROSInterruptException:
        pass
    # Allow ROS to go to all callbacks
    rospy.spin()

if __name__ == '__main__':
    main()