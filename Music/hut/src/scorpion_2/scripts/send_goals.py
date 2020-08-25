#!/usr/bin/env python
#author: akhilraj
#credits: HuT labs

import rospy
import roslib

from std_msgs.msg import String, UInt16
from geometry_msgs.msg import PoseStamped, Twist

arm_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)


def callback(msg):
	
	# Goal1
	goal1 = PoseStamped()
	goal1.header.frame_id = "/map"
	goal1.header.stamp = rospy.Time.now()
	goal1.pose.position.x = 0.864630460739
	goal1.pose.position.y = 1.44200921059
	goal1.pose.position.z = 0.0
	goal1.pose.orientation.x = 0.0
	goal1.pose.orientation.y = 0.0
	goal1.pose.orientation.z = -0.0919628122864
	goal1.pose.orientation.w = 0.99576244213

	# Goal2
	goal2 = PoseStamped()
	goal2.header.frame_id = "/map"
	goal2.header.stamp = rospy.Time.now()
	goal2.pose.position.x = 4.39632034302
	goal2.pose.position.y = 0.251325845718
	goal2.pose.position.z = 0.0
	goal2.pose.orientation.x = 0.0
	goal2.pose.orientation.y = 0.0
	goal2.pose.orientation.z = -0.722276729101
	goal2.pose.orientation.w = 0.691604169015

	# Goal3
	goal3 = PoseStamped()
	goal3.header.frame_id = "/map"
	goal3.header.stamp = rospy.Time.now()
	goal3.pose.position.x = 4.35864925385
	goal3.pose.position.y = -3.35894012451
	goal3.pose.position.z = 0.0
	goal3.pose.orientation.x = 0.0
	goal3.pose.orientation.y = 0.0
	goal3.pose.orientation.z = 0.734032963094
	goal3.pose.orientation.w = 0.679113841039

	# Goal4
	goal4 = PoseStamped()
	goal4.header.frame_id = "/map"
	goal4.header.stamp = rospy.Time.now()
	goal4.pose.position.x = -3.14644575119
	goal4.pose.position.y = 1.14323961735
	goal4.pose.position.z = 0.0
	goal4.pose.orientation.x = 0.0
	goal4.pose.orientation.y = 0.0
	goal4.pose.orientation.z = -0.512164065312
	goal4.pose.orientation.w = 0.858887635377

	# Goal5
	goal5 = PoseStamped()
	goal5.header.frame_id = "/map"
	goal5.header.stamp = rospy.Time.now()
	goal5.pose.position.x = 0.0416490510106
	goal5.pose.position.y = -3.22366309166
	goal5.pose.position.z = 0.0
	goal5.pose.orientation.x = 0.0
	goal5.pose.orientation.y = 0.0
	goal5.pose.orientation.z = 0.708835424467
	goal5.pose.orientation.w = 0.705373901574




	if msg.data == 1:
		rospy.loginfo("Goal1")
		arm_pub.publish(goal1)

	elif msg.data == 2:
		rospy.loginfo("Goal2")
		arm_pub.publish(goal2)

	elif msg.data == 3:
		rospy.loginfo("Goal3")
		arm_pub.publish(goal3)

	elif msg.data == 4:
		rospy.loginfo("Goal4")
		arm_pub.publish(goal4)

	elif msg.data == 5:
		rospy.loginfo("Goal5")
		arm_pub.publish(goal5)
	else:
		rospy.loginfo("zzzzzz")


def callback_cord(msg):
	cord = PoseStamped()
	cord.header.frame_id = "/map"
	cord.header.stamp = rospy.Time.now()
	cord.pose.position.x = msg.linear.x
	cord.pose.position.y = msg.linear.y
	cord.pose.position.z = 0.0
	cord.pose.orientation.x = 0.0
	cord.pose.orientation.y = 0.0
	cord.pose.orientation.z = 0.220796525578
	cord.pose.orientation.w = 0.975319893313
	

	rospy.loginfo("cord")
	arm_pub.publish(cord)


def loop():
	rospy.sleep(1)	
	rospy.init_node("send_goal")
	rospy.Subscriber("bt", UInt16, callback)
	
	rospy.Subscriber("scale_cord", Twist, callback_cord)	

	rospy.spin()

loop()




