#!/usr/bin/env python
import time
import roslib  #roslib.load_manifest('ur_driver')
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
from std_msgs.msg import Float64

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
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

rospy.init_node("test_move", anonymous=True, disable_signals=True)
pub0 = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
pub1 = rospy.Publisher('/linx_controller/command', Float64, queue_size=10)
rate = rospy.Rate(10)
anga=0
angb=0
angc=0
angd=0
ange=0
angf=0
while(True):
	anga+=0.1

	if anga>=1.5:
		anga=0
	Q1=[anga,angb,angc,angd,ange,angf]
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
	pub0.publish(traj)
	pub1.publish(2)
	rate.sleep()
	
