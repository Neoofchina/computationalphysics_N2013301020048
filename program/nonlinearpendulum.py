from math import *
import matplotlib.pyplot as pyp
import matplotlib.pyplot as plt
N=input('N=')
dt=input('dt=')
t=[dt*i for i in range(N)]
def peak(a,b,c): #寻峰寻谷
    if a<b and b>c:
       ans=1
    elif a>b and b<c:
          ans=-1
    else:
          ans=0
    return ans
def EulerCromer(theta0,w0,s,c):
    theta=[None]*N
    w=[None]*N
    theta[0]=theta0
    w[0]=w0
    hT=[None]*20
    n=0
    for i in range(N-1):
        w[i+1]=w[i]-9.8*sin(theta[i])*dt
        theta[i+1]=theta[i]+w[i+1]*dt
        if i>1:
            p=peak(theta[i-2],theta[i-1],theta[i])
            if p==1 or p==-1:
                hT[n]=dt*(i-1)
                n=n+1
    S=0
    for i in range(n-1):
        hT[i+1]=hT[i+1]-hT[0]
        S=hT[i+1]+S
    if n==0:
        aveT=0
    else:
        aveT=4*S/((n+1)*n)
    if c==1:
       pyp.plot(t,theta,label=s)
    return aveT

def change():
    theta=[pi*(i+1)/(2*N) for i in range(N)]
    T=[None]*N
    for i in range(N):
        T[i]=EulerCromer(theta[i],0,'theta0=pi/2,w0=0',0)
    plt.plot(theta,T,label='10000,0.001')
    return None

#a1=EulerCromer(pi/2,0,'theta0=pi/2,w0=0',1)
#a2=EulerCromer(pi/3,0,'theta0=pi/3,w0=0',1)
b=change()  
pyp.legend(loc="upper right", frameon=False)
pyp.xlabel('t/s')
pyp.ylabel('theta/rad')
pyp.title('Nonlinear pendulum')
plt.legend(loc="upper right", frameon=False)
plt.xlabel('theta0/rad')
plt.ylabel('T/s')
plt.title('T vary with theta0')
