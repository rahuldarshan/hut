#!/usr/bin/env python

import rospy
import os
#import subprocess
from std_msgs.msg import Float32

rospy.init_node('parameter')

def parameter():
        
        
	speed=0.0
        rospy.loginfo("accelerating")
	while(speed<50.0):
        	os.system("rosrun dynamic_reconfigure dynparam set /move_base/TrajectoryPlannerROS max_vel_x "+str(speed))
		speed=speed+3
		rospy.sleep(2)

	rospy.spin()


if __name__ == '__main__':
    try:
        parameter()
    except rospy.ROSInterruptException:
        pass

