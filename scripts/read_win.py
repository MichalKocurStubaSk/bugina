#!/usr/bin/env python


import rospy

form std_msgs.msg import Header

def callback(msg):
  
if __name__ == '__main__':
    try:

        rospy.init_node('scan_header')
        sub = rospy.Subscriber("/msg_header",std_msgs::Header,callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

