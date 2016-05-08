# -*- coding: utf-8 -*-
"""
Created on Sun May 08 09:53:56 2016

@author: 李尧
"""

import matplotlib.pyplot as p
from math import *
class star():
    def __inti__(self,condition):
        self.m=condition[0]
        self.x=condition[1]
        self.y=condition[2]
        self.vx=condition[3]
        self.vy=condition[4]
        return None
    def interact(self,ob,n,dt):
        r=((self.x-ob.x)**2+(self.y-ob.y)**2)**0.5
        self.vx=self.vx-4*pi*pi*(self.x-ob.x)*dt*ob.m/(r)**(1+n)
        self.vy=self.vy-4*pi*pi*(self.y-ob.y)*dt*ob.m/(r)**(1+n)
        return None
    def move(self,dt):        
        self.x=self.x+self.vx*dt
        self.y=self.y+self.vy*dt
        return None
    def state(self):
        state=[self.x,self.y,self.vx,self.vy]        
        return state
def ellipticalcondition(ms,mp,a,e,theta):
    x=a*cos(theta)
    y=a*sin(theta)
    v=(4*pi*pi*(1-e)*(ms+mp)/a/(1+e))**0.5
    vx=-v*sin(theta)
    vy=v*cos(theta)
    return [mp,x,y,vx,vy]
earth=star()
condition3=ellipticalcondition(1,1/3*10**(-6),1,0.017,0)
condition32=[condition3[0],condition3[1],condition3[2],condition3[3]/(1+condition3[0]),condition3[4]/(1+condition3[0])]
earth.__inti__(condition32)
sun=star()
condition0=[1,0,0,-condition3[3]*condition3[0]/(1+condition3[0]),-condition3[4]*condition3[0]/(1+condition3[0])]
sun.__inti__(condition0)
mercury=star()
condition1=ellipticalcondition(1,1.2*10**(-7),0.39,0.206,7/180*pi)
mercury.__inti__(condition1)
venus=star()
condition2=ellipticalcondition(1,2.45*10**(-6),0.72,0.007,3.4/180*pi)
venus.__inti__(condition2)
mars=star()
condition4=ellipticalcondition(1,3.3*10**(-7),1.52,0.093,1.9/180*pi)
mars.__inti__(condition4)
jupiter=star()
condition5=ellipticalcondition(1,9.5*10**(-4),5.2,0.048,1.3/180*pi)
jupiter.__inti__(condition5)
saturn=star()
condition6=ellipticalcondition(1,2.85*10**(-4),9.54,0.056,2.5/180*pi)
saturn.__inti__(condition6)
uranus=star()
condition7=ellipticalcondition(1,4.4*10**(-5),19.19,0.046,0.8/180*pi)
uranus.__inti__(condition7)
neptune=star()
condition8=ellipticalcondition(1,5.15*10**(-5),30.06,0.01,1.8/180*pi)
neptune.__inti__(condition8)
s=[sun,earth]
N=20000
dt=0.001
x0=[]
y0=[]
x3=[]
y3=[]
x1=[]
y1=[]
x2=[]
y2=[]
x4=[]
y4=[]
x5=[]
y5=[]
x6=[]
y6=[]
x7=[]
y7=[]
x8=[]
y8=[]
x=[x0,x3,x2,x1,x4,x5,x6,x7,x8]
y=[y0,y3,y2,y1,y4,y5,y6,y7,y8]
for i in range(N):
    for j in range(2):
        state=s[j].state()
        x[j].append(state[0])
        y[j].append(state[1])
    for j in range(2):
        for k in range(2):
            if j==k:
                continue
            else:
               s[j].interact(s[k],3.01,dt)
    for j in range(2):
        s[j].move(dt)
p.plot(x3,y3,label='earth')
p.plot(x0,y0,'*',label='sun')
#p.plot(x1,y1,label='mercury')
#p.plot(x2,y2,label='venus')
#p.plot(x4,y4,label='mars')
#p.plot(x5,y5,label='jupiter')
#p.plot(x6,y6,label='saturn')
#p.plot(x7,y7,label='uranus')
#p.plot(x8,y8,label='neptune')
p.xlabel('x')
p.ylabel('y')
p.title('orbit of earth if n=3.01')
p.legend(loc="upper right", frameon=False)    