#!/usr/bin/env python

import rospy
import random
#from mega_bot.msg import WheelSpeed
from std_msgs.msg import Float32MultiArray

#speed = WheelSpeed()

def speedGenerator():
    pub = rospy.Publisher('plcreadpub', Float32MultiArray, queue_size=10)
    rospy.init_node('fake_speed_generator', anonymous=True)
    rate = rospy.Rate(50) # 20hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #speed = [1.1 , 1.2 , 1.1 , 1.2]
        #speed.frontLeft = 0.00 + random.uniform(0, 0.01)
        #speed.frontRight = 0.00 + random.uniform(0, 0.01)
        #speed.rearLeft = 0.00 + random.uniform(0, 0.01)
        #speed.rearRight = 0.00 + random.uniform(0, 0.01)
        Fi_Volant_act = 0.1 + random.uniform(0, 0.01)
        Speed_Wheel_Left = 1.0 + random.uniform(0, 0.01)
        Speed_Wheel_Right = 0.95 + random.uniform(0, 0.01)
        rospy.loginfo(Fi_Volant_act)
        rospy.loginfo(Speed_Wheel_Left )
        rospy.loginfo(Speed_Wheel_Right)
        pub.publish(Float32MultiArray(data=[Fi_Volant_act,Speed_Wheel_Left,Speed_Wheel_Right]))
        rate.sleep()

if __name__ == '__main__':
    try:
        speedGenerator()
    except rospy.ROSInterruptException:
        pass
