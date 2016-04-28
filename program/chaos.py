# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:37:32 2016

@author: 李尧
"""
from math import *
import matplotlib.pyplot as p
def ln(n):
    if n<1:
      x=n-1
      y=0
      for i in range(50):
         y=y+x**(i+1)
    elif n==1 :
        y=0
    else:
        y=-ln(1/n)
    return y    
class boxes():
    def __inti__(self,e,m,n):
        self.e=e
        self.m=m
        self.n=n
        self.box=[0]*((2*m+1)*(2*n+1))
        self.N=0
        self.I=0
    def count(self,x,y):
        mi=int(x/self.e)
        ni=int(y/self.e)
        if mi<self.m and mi>-self.m:
            if ni<self.n and ni>-self.n:
                self.box[(mi+self.m)*self.n+ni]=1+self.box[(mi+self.m)*self.n+ni]
                self.N+=1
        
        return None
    def dimension(self):
  
        m=self.m
        n=self.n
        if self.N==0:
            d=None
        else:
           for i in range(2*m+1):
               for j in range(2*n+1):
                    p=float(self.box[(i-m)*n+j])/float(self.N)
                   
                    if p==0:
                        continue
                    else:
                        self.I=self.I+p*ln(p)
        
        d1=self.I/ln(self.e)
        d2=-ln(self.N)/ln(self.e)
        print(d1,d2)
        return None
b=boxes()
b.__inti__(0.005,2000,1000)
class nonlinearpendulum():
    def __int__(self,Fd,Tt,dt,N,theta0,w0):
        self.g=9.8
        self.l=9.8
        self.Fd=Fd
        self.Td=Tt
        self.N=N
        self.dt=dt
        self.theta=[theta0]*N
        self.w=[w0]*N
        self.q=0.5
        self.t=[i*dt for i in range(N)]
       
    def caculate(self,j):
        for i in range(self.N-1):
            self.w[i+1]=self.w[i]+self.dt*(-self.g/self.l*sin(self.theta[i])-self.q*self.w[i]+self.Fd*sin(2*pi/self.Td*i*self.dt))
            self.theta[i+1]=self.theta[i]+self.dt*self.w[i+1]
            while self.theta[i+1]>pi:
                self.theta[i+1]=self.theta[i+1]-2*pi
            while self.theta[i+1]<-pi:
                self.theta[i+1]=self.theta[i+1]+2*pi
           
        if j==0:
            p.plot(self.t,self.theta,'k')
            p.xlabel('t/s')
            p.ylabel('theta/rad ')
            self.theta[0]=self.theta[self.N-1]
            self.w[0]=self.w[self.N-1]
            self.t=[self.t[i]+self.N*self.dt for i in range(self.N)]
            return None 
        elif j==1:
            p.plot(self.theta,self.w,'k')
            p.xlabel('theta/rad')
            p.ylabel('w/rad*s')
            p.title('Fd=1.2')
            self.theta[0]=self.theta[self.N-1]
            self.w[0]=self.w[self.N-1]
            self.t=[self.t[i]+self.N*self.dt for i in range(self.N)]
            return None
        elif j==2:
            n=int(self.dt*self.N/self.Td)
            m=int(self.Td/self.dt)
            theta=[]
            w=[]
            for i in range(n):
               theta.append(self.theta[i*m])  
               w.append(self.w[i*m])
               b.count(theta[-1]-3,w[-1]+1)
            p.plot(theta,w,'k*')
            p.xlabel('Fd')
            p.ylabel('w/rad*s')
         
            self.theta[0]=self.theta[self.N-1]
            self.w[0]=self.w[self.N-1]
            self.t=[self.t[i]+self.N*self.dt for i in range(self.N)]
            return None
        else:
            n=int(self.dt*self.N/self.Td)
            m=int(self.Td/self.dt)
            for i in range(n):
                p.plot(self.Fd,self.theta[i*m],'k*')
            return None
pen=nonlinearpendulum()
pen.__int__(1.2,3*pi,0.005*3*pi,8000,0.2,0)
for i in range(200):
    pen.caculate(2)
    print(i)
