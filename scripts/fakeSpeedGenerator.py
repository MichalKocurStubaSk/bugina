#!/usr/bin/env python

import rospy
import random
from mega_bot.msg import WheelSpeed

speed = WheelSpeed()

def speedGenerator():
    pub = rospy.Publisher('wheel_speed', WheelSpeed, queue_size=10)
    rospy.init_node('fake_speed_generator', anonymous=True)
    rate = rospy.Rate(50) # 20hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #speed = [1.1 , 1.2 , 1.1 , 1.2]
        speed.frontLeft = 0.00 + random.uniform(0, 0.01)
        speed.frontRight = 0.00 + random.uniform(0, 0.01)
        speed.rearLeft = 0.00 + random.uniform(0, 0.01)
        speed.rearRight = 0.00 + random.uniform(0, 0.01)
        
        rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()

if __name__ == '__main__':
    try:
        speedGenerator()
    except rospy.ROSInterruptException:
        pass
