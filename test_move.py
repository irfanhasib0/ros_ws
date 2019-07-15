#!/usr/bin/env python
import time
import roslib  #roslib.load_manifest('ur_driver')
import rospy
import actionlib
from control_msgs.msg import *
from sensor_msgs.msg import Image ,LaserScan, JointState
from trajectory_msgs.msg import *
from std_msgs.msg import Float64
from ikyne import kinematics

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
ur_kin=kinematics(1,1,1,1)
Q1 = [2.2,0,-1.57,0,0,0]
Q2 = [1.5,0,-1.57,0,0,0]
Q3 = [1.5,-0.2,-1.57,0,0,0]


Q1 = [0,0,0,0,0,0]
Q2 = [0,0,0,0,0,0]
Q3 = [0,0,0,0,0,0]

client = None
#g = FollowJointTrajectoryGoal()
traj = JointTrajectory()
traj.joint_names = JOINT_NAMES
fb_joints=[]
fb_names=[]
def cb_joint_states(data):
        global fb_joints,fb_names
        #print('received')
        fb_joints=list(data.position)
        fb_names=list(data.name)
rospy.init_node("test_move", anonymous=True, disable_signals=True)
pub0 = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
box1_x = rospy.Publisher('/box1_linx_controller/command', Float64, queue_size=10)
box1_y = rospy.Publisher('/box1_liny_controller/command', Float64, queue_size=10)
def box1_pub(x,y):
	box1_x.publish(x)
	box1_y.publish(y)
rospy.Subscriber("joint_states",JointState, cb_joint_states)


rate = rospy.Rate(10)
anga=0
angb=0
angc=0
angd=0
ange=0
angf=0
#['elbow_joint', 'linx_joint', 'liny_joint', 'shoulder_lift_joint', 'shoulder_pan_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
fb_anga=0
fb_angb=0
fb_angc=0
fb_linx=0
fb_liny=0

while(True):
	anga+=0.1

	if anga>=1.5:
		anga=0
	Q1=[anga,angb,angc,angd,ange,angf]
	try:
		fb_anga=fb_joints[fb_names.index('shoulder_pan_joint')]
		fb_angb=fb_joints[fb_names.index('shoulder_lift_joint')]
		fb_angc=fb_joints[fb_names.index('elbow_joint')]
		fb_linx=fb_joints[fb_names.index('box1_linx_joint')]
		fb_liny=fb_joints[fb_names.index('box1_liny_joint')]
	except:0
	#print('fb_anga',fb_anga)
	xx,yy=ur_kin.fkine(fb_anga,fb_angb,fb_angc)
	print(fb_anga,fb_angb,fb_angc,fb_linx,fb_liny)
	print(xx,yy)
	
	if anga!=0:
		traj.points = [
			JointTrajectoryPoint(positions=Q1, velocities=[0]*6, time_from_start=rospy.Duration(0.2))
			#JointTrajectoryPoint(positions=Q2, velocities=[0]*6, time_from_start=rospy.Duration(3.0)),
			]
	else:
		traj.points = [
			JointTrajectoryPoint(positions=Q1, velocities=[0]*6, time_from_start=rospy.Duration(1.0))
			#JointTrajectoryPoint(positions=Q2, velocities=[0]*6, time_from_start=rospy.Duration(3.0)),
			]
	#pub0.publish(traj)
	box1_pub(1,1)
	rate.sleep()
	
