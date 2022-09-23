#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from inertial_sense_ros.msg import GPS
from sensor_msgs.msg import NavSatFix

class publishGPS(object):

	def __init__(self):
		rospy.loginfo("Initialising INS odometry publishing")
		self.gps_sub=rospy.Subscriber('/ins',Odometry, self.callback, queue_size=1)
		self.lastMsg=Odometry()
		self.gps_pub=rospy.Publisher('/odometry_ins', Odometry, queue_size=1)
		rospy.sleep(8)
		rospy.loginfo("initialised")

	def callback(self, data):
		self.lastMsg=data

	def do_work(self):
		#self.splitStrings= str(self.lastMsg).split(",")
		gpsmsg=self.lastMsg
		gpsmsg.pose.pose.position.x=gpsmsg.pose.pose.position.x-5350893.0
		gpsmsg.pose.pose.position.y=gpsmsg.pose.pose.position.y-1896947.25
		gpsmsg.pose.pose.position.z=0.0
		#gpsmsg.header.frame_id = "gps"
		#rospy.loginfo(self.splitStrings[1])
		#gpsmsg.latitude=self.lastMsg.latitude
		#gpsmsg.longitude=self.lastMsg.longitude 
		#gpsmsg.position_covariance_type=0
		self.gps_pub.publish(gpsmsg)

	def run(self):
		r=rospy.Rate(20)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()

if __name__=='__main__':
	rospy.init_node('pubgps')
	obj=publishGPS()
	obj.run()