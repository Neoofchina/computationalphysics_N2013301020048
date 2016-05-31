# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:05:04 2016

@author: 李尧
"""

import matplotlib.pyplot as p
import matplotlib.animation as a
from math import *
class wave():
    def __inti__(self,y0,r,dt,dx):
       
        self.y=[[0 for i in range(len(y0)) ] for i in range(3)]
        
        self.r=r
        self.dt=dt
        self.dx=dx
        self.x=[i*dx for i in range(len(y0))]
        N=0
        for i in range(len(y0)):
            N=N+y0[i]
        self.N=N
        self.y[1]=y0
        self.y[0]=y0
    def fixedboundary(self):
         
        for j in range(len(self.y[0])-2):
                self.y[2][j+1]=2*(1-self.r**2)*self.y[1][j+1]-self.y[0][j+1]+(self.r**2)*(self.y[1][j+2]+self.y[1][j])
                
        self.y[0]=self.y[1]
        self.y[1]=self.y[2] 
        self.y[2]=[0.0 for i in range(len(self.y[1]))]
        return None
def updata(i):
    w.fixedboundary()
    line.set_data(w.x,w.y[1])
    return line  
def init():
    line,=windows.plot(w.x,w.y[1])
    return line
w=wave()
N=300
#y0=[0.0 for i in range(N)]
#for i in range(100):
#    y0[i+50]=1.0
y01=[exp(-0.01*(i-200)**2) for i in range(N)]
y02=[0.0 for i in range(N)]
for i in range(20):
    y02[i+50]=1.0*i/19
    y02[i+70]=-1.0*i/19+1.0
y0=[y01[i]+y02[i] for i in range(N)]
w.__inti__(y0,1.0,0.1,0.1)
f=p.figure()
windows=f.add_subplot(111)

line,=p.plot(w.x,w.y[1])
#for i in range(300):
    #p.plot(w.x,w.y[1],label=str(i))
    #updata()
anim1=a.FuncAnimation(f, updata, init_func=init, frames=30000, interval=10)
p.ylim(-1.0,1.0)    
p.show()
#line,=p.plot(w.x,w.y[1],label='f')

      
