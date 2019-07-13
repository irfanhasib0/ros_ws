#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image ,LaserScan
import numpy as np
import cv2
def callback(data):
	img=(data.ranges[0])
	#cv2.imshow('img',img)
	#cv2.waitKey(10)
	print(img)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/rrbot/laser/scan",LaserScan, callback)
	
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
