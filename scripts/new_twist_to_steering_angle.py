#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist

rospy.init_node('twist_to_steering_angle')

def sender(steer_value, loc_target_speed ):
    pub2 = rospy.Publisher('sub_steer', Float64, queue_size=10)
    pub3 = rospy.Publisher('target_speed', Float64, queue_size=10)
    pub4 = rospy.Publisher('ref_speed_steer', Float64MultiArray, queue_size=10)
    rate = rospy.Rate(30) # hz
    #print("tspeed:" + str(loc_target_speed))
    pub2.publish(steer_value)
    pub3.publish(loc_target_speed)
    array = [steer_value,loc_target_speed]
    my_array_for_publishing = Float64MultiArray(data=array)
    pub4.publish(my_array_for_publishing)
    rate.sleep()

def callback1(data):
    global target_speed
    global angular_speed

    target_speed = data.linear.x
    
    angular_speed = data.angular.z

    wheelbase = 1.1
    steer_us = 1455

    if angular_speed == 0:
        steer_deg = 0
    else:
        radius = target_speed / angular_speed
        steer_deg = math.degrees(math.atan(wheelbase / radius))
        #steer_us = steer_deg * 16.12 + 1455

    
    sender(float(steer_deg), float(target_speed))

rospy.Subscriber("cmd_vel", Twist, callback1)
rospy.spin()