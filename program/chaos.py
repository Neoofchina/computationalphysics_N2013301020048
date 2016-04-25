# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:37:32 2016

@author: 李尧
"""
from math import *
import matplotlib.pyplot as p
class nonlinearpendulum():
    def __int__(self,Fd,Tt,dt,N,theta0,w0):
        self.g=9.8
        self.l=9.8
        self.Fd=Fd
        self.Td=Tt
        self.N=N
        self.dt=dt
        self.theta=[theta0]
        self.ftheta=[theta0]
        self.w=[w0]
        self.q=0.5
        self.t=[i*dt for i in range(N)]
    def caculate(self):
        for i in range(self.N-1):
            self.w.append(self.w[-1]+self.dt*(-self.g/self.l*sin(self.theta[-1])-self.q*self.w[-1]+self.Fd*sin(2*pi/self.Td*i*self.dt)))
            self.theta.append(self.theta[-1]+self.dt*self.w[-1])
            while self.theta[-1]>pi:
                self.theta[-1]=self.theta[-1]-2*pi
            while self.theta[-1]<-pi:
                self.theta[-1]=self.theta[-1]+2*pi
            self.ftheta.append(self.theta[-1])
        return None
    def result(self,j,t):
        if j==0:
            p.plot(self.t,self.theta,label='t-theta')
            p.xlabel('t/s')
            p.ylabel('theta/rad ')
            return None 
        elif j==1:
            p.plot(self.t,self.ftheta,label='t-ftheta')
            p.xlabel('t/s')
            p.ylabel('theta/rad ')
            p.title('Fd=1.2')
            return None
        elif j==2:
            p.plot(self.ftheta,self.w,label='theta-w')
            p.xlabel('theta/rad')
            p.ylabel('w/rad*s')
            p.title('Fd=1.2')
            return None
        else:
            n=int(self.dt*self.N/self.Td)
            m=int(self.Td/self.dt)
            theta=[]
            w=[]
            for i in range(n):
               theta.append(self.ftheta[i*m])  
               w.append(self.w[i*m])
            if t==1:
               p.plot(theta,w,'*',label='strange attractor')
               p.xlabel('theta/rad')
               p.ylabel('w/rad*s')
            return theta
            

c1=input('c1=')
if c1==0:
   pen0=nonlinearpendulum()
   pen0.__int__(1.2,3*pi,0.0001,5000000,0.2,0)
   pen0.caculate()
  #pen0.result(1,1)
   theta=pen0.result(3,1)
   #pen0.result(2,1)
else:
   pen1=nonlinearpendulum()
   pen1.__int__(1.2,3*pi,0.01,400000,0.2,0)
   F=[i*0.1 for i in range(20)]
   for i in range(15):
       pen1.Fd=F[i]
       pen1.caculate()
       m=int(pen1.Td/pen1.dt)
       n=int(pen1.dt*pen1.N/pen1.Td)
       theta=[theta[i*m] for i in range(n)]
       for j in range(n-300):
          p.plot(F[i],theta[j+300],'k*')
    
       
       



            