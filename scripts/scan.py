#!/usr/bin/env python

import rospy

from geometry_msgs.msg import PoseStamped

from sensor_msgs.msg  import LaserScan

range_0_array = [0,0,0,0,0,0,0,0,0,0]
range_90_array = [0,0,0,0,0,0,0,0,0,0]


def callback(msg):
    del range_0_array[0]
    del range_90_array[0]
    range_0_array.append(msg.ranges[0])
    range_90_array.append(msg.ranges[90])
    #print range_0_array
    print "range 0 priemer z 10 poslednych"
    range_0_priemer = sum(range_0_array)/10
    print range_0_priemer
    print "range 90 priemer z 10 poslednych"
    range_90_priemer = sum(range_90_array)/10
    print range_90_priemer

    #h = std_msgs.msg.Header()
    #h.stamp = rospy.Time.now()
    p = PoseStamped()
    p.pose.position.x = range_0_priemer
    p.pose.position.y = range_90_priemer
    p.pose.position.z = 0

    p.pose.orientation.x = 0
    p.pose.orientation.y = 0
    p.pose.orientation.z = 0
    p.pose.orientation.w = 1.0
    p.header.stamp = rospy.Time.now()
    pub.publish(p)
    #print "size of array"
    #print len(msg.ranges)
    #print "value at 0 degrees"
    #print msg.ranges[0]
    #print "value at 90 degrees"
    #print msg.ranges[90]


if __name__ == '__main__':
    try:

        rospy.init_node('scan_decode')
        pub = rospy.Publisher('lidarxy',PoseStamped, queue_size = 10)
        #rospy.init_node('talker', anonymous=True)
        sub = rospy.Subscriber("scan",LaserScan,callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

