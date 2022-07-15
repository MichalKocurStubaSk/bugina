#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

from nav_msgs.msg import Odometry
from std_msgs.msg import Float32MultiArray

import math
import time
import tf

L = 1.5  #0.66  #rozhod kolies
Ts =  0.02
Theta = 0
X = 0
Y = 0
vX = 0
vY = 0 
seq = 0
otackyMetre = 1.67


def wheelsCallback(wheels):
    global Theta, X, Y, lastMessageTime, seq
    now = rospy.Time.now()
    period = now - lastMessageTime
    seq += 1
    #print 'frontLeft = ', wheelSpd.frontLeft
    #print 'frontRight = ', wheelSpd.frontRight
    #print 'rearLeft = ', wheelSpd.rearLeft
    #print 'rearRight = ', wheelSpd.rearRight

    wheelAngle = -1*wheels.data[0]
    vR = wheels.data[2]
    vL = wheels.data[1]
    vS = wheels.data[3]
    #POZOR UWAGA, toto iba kym je iba lavy senzor
    vR=vL
    #KONIEC UWAGY

    wheelBase=1.5
    #speed= (vR + vL)/ 2.0
    speed= vS*otackyMetre*0.5 #toto je lebo to nejako nevychadzalo
    v_th=speed*math.tan(wheelAngle)/ wheelBase
    vx = speed
    vy = 0.0
    #odomMsg.twist.twist.linear.x = vx
    #odomMsg.twist.twist.linear.y = vy
    #odomMsg.twist.twist.angular.z = v_th
    #odomMsg.header.frame_id = 'odom'
    #odomMsg.child_frame_id = 'base_footprint'

    dTheta = v_th*(period.to_sec())
    dS = vx*(period.to_sec())




    #dLeft = speedLeft*(period.to_sec())
    #dRight = speedRight*(period.to_sec())
    #dS = (dRight+ dLeft)/2
    #vTheta = (speedRight - speedLeft)/(L)
    #dTheta = (dRight - dLeft)/(L)
    dY = dS * math.sin(Theta + (dTheta*0.5))
    dX = dS * math.cos(Theta + (dTheta*0.5))
    
    X = X + dX
    Y = Y + dY


    vX = vx#dX/(period.to_sec())
    vY = vy#dY/(period.to_sec())
    vTheta = v_th#dTheta/(period.to_sec())
    Theta = Theta + dTheta
    #Theta = Theta % (2*math.pi)
    #print "speedLeft = ", vL
    #print "speedRight = ", vR 
    #print "speedShaft = ", vS 
    #print "x = " , X
    #print "y = " , Y
    #print "th= " , Theta
    #print "ts= " , period.to_sec()
  
  
    odom_quat = tf.transformations.quaternion_from_euler(0 , 0, Theta)
    #print "quat = " , odom_quat
    time = rospy.get_rostime()

    #transform tf
    odom_broadcaster.sendTransform(
        (X,Y,0),
        odom_quat,
        time,
        "base_footprint",
        "odom"
    )

    odom = Odometry()

    odom.header.seq = seq
    odom.header.stamp = now   
    odom.header.frame_id = "odom"
    # postion
    odom.pose.pose = Pose(Point(X,Y,0.0), Quaternion(*odom_quat))

    # velocity
    odom.child_frame_id = "base_footprint"
    odom.twist.twist = Twist(Vector3(vX,vY, 0.0), Vector3(0, 0, vTheta))

    # send odomerty
    odom_publisher.publish(odom)
    lastMessageTime = now



if __name__ == '__main__':
    try:
        rospy.init_node('odom_from_speed', anonymous=True)
        lastMessageTime = rospy.get_rostime()
        wheels_topic = "PLCreadpub"
        speed_subsciber = rospy.Subscriber(wheels_topic, Float32MultiArray, wheelsCallback)
        odom_publisher = rospy.Publisher('odom', Odometry, queue_size=10) 
        odom_broadcaster = tf.TransformBroadcaster()

        rospy.spin()
        

    except rospy.ROSInterruptException:
        pass