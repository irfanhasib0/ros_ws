#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory , JointTrajectoryPoint
import time
import numpy as np
def talker():
    pub1 = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    #pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    ang1=0
    ang2=0
    ang3=0
    i=0
    names=['shoulder_pan_joint','shoulder_lift_joint','elbow_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint']
    while not rospy.is_shutdown():
        positions_goal=np.zeros(len(names),dtype=np.float64)
        
        positions_goal[0]=ang1
        positions_goal[1]=ang2
        positions_goal[2]=ang3
        jt = JointTrajectory()
        jt.joint_names = names
        jt.header.stamp = rospy.Time.now()
        jtp = JointTrajectoryPoint()
        jtp.positions = positions_goal
        jtp.velocities = np.zeros(len(positions_goal))
        jtp.time_from_start = rospy.Duration(1)
        jt.points = [jtp]
        
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(ang1)
        pub1.publish(jt)
        #pub2.publish(ang2)
        rate.sleep()
        ang1=ang1+.1
        ang2=ang2-.1
        ang3=ang3+.1
        if ang1>=1.5:
			ang1=0
        if ang2<=-1.5:
            ang2=0
        if ang3>=1.5:
            ang3=0

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
