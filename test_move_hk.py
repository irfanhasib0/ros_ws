#!/usr/bin/env python
import rospy, tf
import geometry_msgs.msg, nav_msgs.msg
from std_msgs.msg import Float64
from math import *
pose=[]
def huskyOdomCallback(message):
    global pose
    #print('callback')
    pos = message.pose.pose
    quat = pos.orientation
    # From quaternion to Euler
    angles = tf.transformations.euler_from_quaternion((quat.x,quat.y,
                                                       quat.z,quat.w))
    theta = angles[2]
    pose = [pos.position.x, pos.position.y, theta]  # X, Y, Theta
    
    #print('huskyOdomCallback: x=%4.1f,y=%4.1f dist=%4.2f, cmd.v=%4.2f, cmd.w=%4.2f\n'%(pose[0],pose[1]))
    rate.sleep()
########################################
# Main Script
# Initialize our node
rospy.init_node('nre_simhuskycontrol',anonymous=True)
rate = rospy.Rate(10)


cmdmsg = geometry_msgs.msg.Twist()
cmdpub = rospy.Publisher('/cmd_vel',geometry_msgs.msg.Twist, queue_size=10)
box1_x = rospy.Publisher('/box1_linx_controller/command', Float64, queue_size=10)
box1_y = rospy.Publisher('/box1_liny_controller/command', Float64, queue_size=10)
def box1_pub(x,y):
	box1_x.publish(x)
	box1_y.publish(y)
rospy.Subscriber('/odometry/filtered',nav_msgs.msg.Odometry,huskyOdomCallback)
while(1):
	xx=float(input())
	aa=float(input())
	cmdmsg.linear.x = xx
	cmdmsg.angular.z= aa
	cmdpub.publish(cmdmsg)
	box1_pub(0,0)
	print(pose)
	rate.sleep()
