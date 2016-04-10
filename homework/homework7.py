#**Homework7**
import matplotlib.pyplot as pyp
from math import *
[windx,windy]=input('wind=')
[spinx,spiny,spinz]=input('spin=')
[vx0,vy0,vz0]=input('v=')
N=input('N=')
dt=input('dt=')
def cross(s1,s2,s3,v1,v2,v3):
   c1=s2*v3-s3*v2
   c2=v1*s3-v3*s1
   c3=s1*v2-s2*v1
   return [c1,c2,c3]
def ad(s1,s2,s3,v1,v2,v3):
    c1=s1+v1
    c2=s2+v2
    c3=s3+v3
    return [c1,c2,c3]
def length(s1,s2,s3):
    c1=s1**2
    c2=s2**2
    c3=s3**2
    return (c1+c2+c3)**0.5
vx=[None]*N
vx[0]=vx0
vy=[None]*N
vy[0]=vy0
vz=[None]*N
vz[0]=vz0
x=[0]*N
y=[0]*N
z=[0]*N
for i in range(N-1):
    vw=[vx[i]-windx,vy[i]-windy,vz[i]] 
    l=length(vw[0],vw[1],vw[2])
    b=0.0039+0.0058/(1+exp(((l-35)/5)))
    fa=[-b*l*vw[j] for j in range(3)]
    s=cross(spinx,spiny,spinz,vw[0],vw[1],vw[2])
    fs=[4.1*10**(-4)*s[n] for n in range(3)]
    vx[i+1]=vx[i]+dt*(fa[0]+fs[0])
    vy[i+1]=vy[i]+dt*(fa[1]+fs[1])
    vz[i+1]=vz[i]+dt*(fa[2]+fs[2]-9.8)
    x[i+1]=x[i]+vx[i+1]*dt
    y[i+1]=y[i]+vy[i+1]*dt
    z[i+1]=z[i]+vz[i+1]*dt
    if z[i+1]<0:
        z[i+1]=0
        break
pyp.plot(x,z,label='spin(0,0,0)')
pyp.xlabel('x/m')
pyp.ylabel('y/m')
pyp.legend(loc="upper right", frameon=False)
pyp.title('wind=(10,0,0),v=(31.8,0,31.8),g=9.8')
