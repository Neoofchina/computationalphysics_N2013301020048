from math import *
import matplotlib.pyplot as pyp
import numpy.random as ran
mass=1
v0=input('v0=')
angle=input('angle=')
a0=input('a0=')
h0=input('h0=')
x0=0
y0=0
g=9.8    
def idealfire(N,dt):
    x=[None]*N
    y=[None]*N
    vx=[None]*N
    vy=[None]*N
    vx[0]=v0*cos(angle)
    vy[0]=v0*sin(angle)
    x[0]=x0
    y[0]=y0
    for i in range(N-1):
        vx[i+1]=vx[i]
        vy[i+1]=vy[i]-g*dt
        x[i+1]=x[i]+vx[i+1]*dt
        y[i+1]=y[i]+vy[i+1]*dt
        if y[i+1]<0:
            y[i+1]=0
            break
    p1=pyp.plot(x,y,'black')
    return None
def airdragfire(N,dt):
    x=[None]*N
    y=[None]*N
    v=[None]*N
    vx=[None]*N
    vy=[None]*N
    v[0]=v0
    vx[0]=v0*cos(angle)
    vy[0]=v0*sin(angle)
    x[0]=x0
    y[0]=y0
    for i in range(N-1):
        f=a0*exp(-y[i]/h0)*v[i]**2
        if vx[i]>0:
           vx[i+1]=vx[i]-f*vx[i]/v[i]*dt
        else:
            vx[i+1]=0
        vy[i+1]=vy[i]-(g+f*vy[i]/v[i])*dt
        v[i+1]=abs((vx[i+1]**2+vy[i+1]**2)**0.5)
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
        if y[i+1]<0:
            y[i+1]=0
            break
    p2=pyp.plot(x,y,'red')
    return None
def withwindfire(N,dt,w,u): #w is the viciloty of the wind, and for 2-D model, w has no y-conponent
    x=[None]*N
    y=[None]*N
    v=[None]*N
    vx=[None]*N
    vy=[None]*N
    vx[0]=v0*cos(angle)
    vy[0]=v0*sin(angle)
    v[0]=v0
    x[0]=x0
    y[0]=y0
    for i in range(N-1):
        r=ran.random()
        f=a0*exp(-y[i]/h0)*((vx[i]+w+u*r)**2+(vy[i])**2)
        vx[i+1]=vx[i]-f*(vx[i]+w+u*r)/((vx[i]+w+u*r)**2+(vy[i])**2)**0.5*dt
        vy[i+1]=vy[i]-(g+f*vy[i]/((vx[i]+w+u*r)**2+(vy[i])**2)**0.5)*dt
        v[i+1]=abs((vx[i+1]**2+vy[i+1]**2)**0.5)
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
        if y[i+1]<0:
            y[i+1]=0
            break
    p3=pyp.plot(x,y,'green')
    return None
def smartfire(N,dt,w,u,m):
    x=[None]*N
    y=[None]*N
    vx=[None]*N
    vy=[None]*N
    vx[0]=v0*cos(angle)
    vy[0]=v0*sin(angle)
    x[0]=x0
    y[0]=y0
    for i in range(N-1):
        r=ran.random()
        f=a0*exp(-y[i]/h0)*((vx[i]+w+u*r)**2+(vy[i])**2)
        if i in [0,1]:
            fm=0
        else:
            if abs(f)<m:
                fm=a0*exp(-y[i-1]/h0)*((vx[i-1]+w+u*r)**2+(vy[i-1])**2)
            else:
                if f>0:
                    fm=m
                else:
                    fm=0-m
        vx[i+1]=vx[i]-(f-fm)*(vx[i]+w+u*r)/((vx[i]+w+u*r)**2+(vy[i])**2)**0.5*dt
        vy[i+1]=vy[i]-(g+(f-fm)*vy[i]/((vx[i]+w+u*r)**2+(vy[i])**2)**0.5)*dt
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
        if y[i+1]<0:
            y[i+1]=0
            break
    p4=pyp.plot(x,y,'blue')
    return None
cannon1=idealfire(2000,0.01)
cannon2=smartfire(2000,0.01,10,1,100)
cannon3=airdragfire(2000,0.01)
cannon4=withwindfire(2000,0.01,10,1)
pyp.xlabel('x/m')
pyp.ylabel('y/m')
pyp.title('the orbits in different fire-models')
