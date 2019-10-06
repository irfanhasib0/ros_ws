import os, sys
import tkinter
import threading as thread
import _thread,time
from subprocess import check_output as cout
from subprocess import call
#import tkMessageBox

top = tkinter.Tk()
canv = tkinter.Canvas(top, bg="blue", height=250, width=300)
os.environ['ROS_MASTER_URI']='http://192.168.11.10:11311/'
os.environ['ROS_IP']='192.168.11.10'

#os.system('. ./master.sh')
#os.system('roscore')
call(["bash","/devel/setup.sh"])


def roscore():
    _thread.start_new_thread(os.system,("roscore",))
    
def rosserial():
	os.system("source devel/setup.sh")
	#_thread.start_new_thread(os.system,("rosrun rosserial_python serial_node.py /dev/ttyUSB0",))
	_thread.start_new_thread(os.system,("rosrun rosserial_python serial_node.py /dev/ttyACM0 57600",))

def rosserial_Ard():
	os.system("source devel/setup.sh")
	_thread.start_new_thread(os.system,("rosrun rosserial_python serial_node.py /dev/ttyUSB0 57600",))
	#_thread.start_new_thread(os.system,("rosrun rosserial_python serial_node.py /dev/ttyACM0 115200",))

def serpub():
	os.system("source devel/setup.sh")
	_thread.start_new_thread(os.system,("rostopic pub toggle_led std_msgs/Empty --once",))
	
def rrbot_launch():
    os.system("source devel/setup.sh")
    _thread.start_new_thread(os.system,("roslaunch husky_gazebo husky_empty_world.launch",))

def rrbot_pub():
    os.system("source devel/setup.sh")
    _thread.start_new_thread(os.system,("rosrun rrbot_comm rrbot_pub.py",))

def cam_sub():
    os.system("source devel/setup.sh")
    _thread.start_new_thread(os.system,("python src/husky_mod/scripts/cam_sub.py",))
def cam1_sub():
    os.system("source devel/setup.sh")
    _thread.start_new_thread(os.system,("rosrun rrbot_comm cam1_sub.py",))

def kill_gzc():
   os.system("killall -9 gzclient")

def killall():
   os.system("./kill.sh")

A = tkinter.Button(top, text ="roscore", command = roscore)
B = tkinter.Button(top, text ="rrbot_launch", command = rrbot_launch)
C = tkinter.Button(top, text ="kill_gzc", command = kill_gzc)
D = tkinter.Button(top, text ="rrbot_pub", command = rrbot_pub)
E = tkinter.Button(top, text ="cam_sub", command = cam_sub)
F = tkinter.Button(top, text ="cam1_sub", command = cam1_sub)
G = tkinter.Button(top, text ="rosserial", command = rosserial )
H = tkinter.Button(top, text ="rosserial_Ard", command = rosserial_Ard )
I = tkinter.Button(top, text ="serpub", command = serpub )
Z = tkinter.Button(top, text ="killall", command = killall)

A.place(x=10,y=20,height=20,width=100)
B.place(x=10,y=40,height=20,width=100)
C.place(x=10,y=60,height=20,width=100)
D.place(x=10,y=80,height=20,width=100)
E.place(x=10,y=100,height=20,width=100)
F.place(x=10,y=120,height=20,width=100)
G.place(x=10,y=140,height=20,width=100)
H.place(x=10,y=160,height=20,width=100)
I.place(x=10,y=180,height=20,width=100)
Z.place(x=10,y=200,height=20,width=100)
canv.pack()

os.system("./ros_kill.sh")
os.system('clear')
print('Running roscore')
roscore()
#time.sleep(10)
#rrbot_launch()
top.mainloop()

killall()
