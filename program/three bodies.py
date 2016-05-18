# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:42:01 2016

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
earth.__inti__(condition3)

n=input('n=')
jupiter=star()
condition5=ellipticalcondition(1,9.5*10**(-4)*n,5.2,0.048,1.3/180*pi)
jupiter.__inti__(condition5)

sun=star()
condition0=[1,-earth.m*earth.x-jupiter.m*jupiter.x,-earth.m*earth.y-jupiter.m*jupiter.y,-earth.m*earth.vx-jupiter.m*jupiter.vx,-earth.m*earth.vy-jupiter.m*jupiter.vy]
sun.__inti__(condition0)



s=[sun,earth,jupiter]
N=120000
dt=0.001
x0=[]
y0=[]
x3=[]
y3=[]
x5=[]
y5=[]
x=[x0,x3,x5]
y=[y0,y3,y5]
for i in range(N):
    for j in range(3):
        state=s[j].state()
        x[j].append(state[0])
        y[j].append(state[1])
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            else:
               s[j].interact(s[k],2,dt)
    for j in range(3):
        s[j].move(dt)

p.plot(x3,y3,label='mercury')
p.plot(x0,y0,label='sun')
p.plot(x5,y5,label='jupiter')
p.xlabel('x')
p.ylabel('y')
p.title('orbit of three bodies if m of jupiter=10mj')
p.legend(loc="upper right", frameon=False) 
