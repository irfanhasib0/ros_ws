#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import Image ,LaserScan, JointState
import numpy as np
import cv2
fb_joints=[]

rospy.init_node('rrbot_env', anonymous=True)
rate = rospy.Rate(10) # 10hz

def cb_joint_states(data):
        global fb_joints
	fb_joints=list(data.position)
	rate.sleep()
       


pub0 = rospy.Publisher('/rrbot/joint0_position_controller/command', Float64, queue_size=10)
pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
pub3 = rospy.Publisher('/rrbot/joint3_position_controller/command', Float64, queue_size=10)
#pub4 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
#pub5 = rospy.Publisher('/rrbot/joint3_position_controller/command', Float64, queue_size=10)
rospy.Subscriber("/rrbot/joint_states",JointState, cb_joint_states)

ang1=.60
ang2=1.5
ang0=1.50

def rrbot_env(ang0,ang1,ang2):
        global fb_joints
        hello_str = "hello world %s" % rospy.get_time()
        
        #rospy.loginfo(ang0)
        pub0.publish(ang0)
        pub1.publish(ang1)
        pub2.publish(ang2)
        pub3.publish(ang1-ang2)
        rate.sleep()
        return fb_joints
   
while(1):
                anga=float(input('anga'))
                angb=float(input('angb'))
                angc=float(input('angc'))
                joints=rrbot_env(anga,angb,angc)
                print(joints)
        
    
