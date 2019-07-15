import numpy as np
class kinematics():
	def __init__(self,l1,l2,l3,l4):
		self.l1=l1
		self.l2=l2
		self.l3=l3
		self.l4=l4
	def fkine(self,anga,angb,angc):
			self.l1=.4
			self.l2=1
			self.l3=1
			self.l4=.4
			px=self.l2*np.sin(angb)+self.l3*np.sin(angb+anga)
			py=self.l2*np.cos(anga)+ self.l3*np.cos(angb+angc)
			xx=(px+self.l4)*np.cos(anga)
			yy=(px+self.l4)*np.sin(anga)
			zz=py+self.l1
			return xx,yy
	def ikyne(self,posx,posy,posz):
	 y1=0
	 self.l1=10
	 self.l2=10
	 x1=np.sqrt(posx*posx+posz*posz+posy*posy);

	 #if x1>25 or x1<5:
	   #return
	 
	 a=(float)((x1*x1)+(y1*y1));

	 b=l1*l1+l2*l2;
	 c=l1*l2;
	 
	 cos_b=(a-b)/(float)(2*c);
	 sin_b=np.sqrt(1-cos_b*cos_b);

	 angb=np.arccos(cos_b);
	 #angb=(angb*180)/3.1415;
	 angb=angb;
	 
	 
	 k1=l1+l2*cos_b;
	 k2=l2*sin_b;
	 
	 anga=np.arctan(y1/float(x1))-np.arctan(k2/float(k1));
	 anga=anga+np.arctan(float(posy/float(x1)));
	 if anga<0:
	  anga=-1*anga;

	 
	  
	 anga=anga+np.arcsin(posy/float(x1));
	 
	 #anga=(anga*180)/3.1416;

	 angc=np.arcsin(posz/float(x1));
	 #angc=(angc*180)/3.1416;
	 angd=angb-anga;
	 angd=angd-90;
	 


	 p=anga;

	 
	 q=angb;
	 anga=np.rad2deg(anga)
	 angb=np.rad2deg(angb)
	 angc=np.rad2deg(angc)
	 return anga,angb,angc,angd

def valc(l):
 v=int(np.cos(l)*100)
 return v
def vals(l):
 v=int(np.sin(l)*100)
 return v

