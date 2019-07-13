#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import Image ,LaserScan
import numpy as np
import cv2
def callback(data):
	img=(data.ranges[0])
	rate.sleep()
	#cv2.imshow('img',img)
	#cv2.waitKey(10)
	print('laser scan value :',img)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    #rospy.init_node('listener', anonymous=True)
    
    rate.sleep()
    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

def talker():
    pub0 = rospy.Publisher('/rrbot/joint0_position_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/rrbot/joint3_position_controller/command', Float64, queue_size=10)
    rospy.Subscriber("/rrbot/laser/scan",LaserScan, callback)
    ang1=.60
    ang2=1.5
    ang0=1.50
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(ang0)
        pub0.publish(ang0)
        pub1.publish(ang1)
        pub2.publish(ang2)
        pub3.publish(ang1-ang2)
        rate.sleep()
        ang0=ang0+.1
        #ang1=ang1+.1
        #ang2=ang2+.1
        if ang0>=2.0:
			ang0=1.0
        #if ang1>=1.5:
		#	ang1=.75
        #if ang2>=2.5:
        #    ang2=0

if __name__ == '__main__':
    try:
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        talker()
        listener()
        
    except rospy.ROSInterruptException:
        pass
