import os, sys
import tkinter
import threading as thread
import _thread,time
from subprocess import check_output as cout
from subprocess import call
#import tkMessageBox


os.environ['ROS_MASTER_URI']='http://192.168.11.7:11311/'
os.environ['ROS_IP']='192.168.11.4'
os.system('rostopic list')
#os.system('rostopic echo /odometry/filtered')
#os.system('rostopic type /arm_controller/command/')
os.system('python test_move_hk.py')


