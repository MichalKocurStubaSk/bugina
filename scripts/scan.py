#!/usr/bin/env python

import rospy

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
    #print "size of array"
    #print len(msg.ranges)
    #print "value at 0 degrees"
    #print msg.ranges[0]
    #print "value at 90 degrees"
    #print msg.ranges[90]


if __name__ == '__main__':
    try:

        rospy.init_node('scan_decode')
        sub = rospy.Subscriber("scan",LaserScan,callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

