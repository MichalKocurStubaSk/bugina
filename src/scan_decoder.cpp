

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sensor_msgs/LaserScan.h"

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
// %Tag(CALLBACK)%
//void chatterCallback(const std_msgs::String::ConstPtr& msg)
void chatterCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
  ROS_INFO("I heard: [%f]", msg->ranges[0]);
}
// %EndTag(CALLBACK)%

int main(int argc, char **argv)
{

  ros::init(argc, argv, "scandecoder");

 
  ros::NodeHandle n;

 
// %Tag(SUBSCRIBER)%
  ros::Subscriber sub = n.subscribe("scan", 1000, chatterCallback);
// %EndTag(SUBSCRIBER)%

 
// %Tag(SPIN)%
  ros::spin();
// %EndTag(SPIN)%

  return 0;
}
// %EndTag(FULLTEXT)%