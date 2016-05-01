from math import *
import matplotlib.pyplot as p
class lorenz():
    def __inti__(self,x0,y0,z0,a,b,r,N,dt):
        self.a=a
        self.b=b
        self.r=r
        self.N=N
        self.dt=dt
        self.x=[0]*N
        self.y=[0]*N
        self.z=[0]*N
        self.x[0]=x0
        self.y[0]=y0
        self.z[0]=z0
        self.t=[i*dt for i in range(N)]
        return None
    def caculate(self):
       for i in range(self.N-1):
           self.x[i+1]=self.x[i]+self.dt*self.a*(self.y[i]-self.x[i])
           self.y[i+1]=self.y[i]+self.dt*(-self.x[i]*self.z[i]+self.r*self.x[i]-self.y[i])
           self.z[i+1]=self.z[i]+self.dt*(self.x[i]*self.y[i]-self.b*self.z[i])
       return None
    def draw(self,s):
        t='t'
       
        if t in s:
            p.xlabel('t')
            if s[2]=='x':
               p.plot(self.t,self.x)
               p.ylabel('x')
            elif s[2]=='y':
               p.plot(self.t,self.y)
               p.ylabel('y')
            else:
               p.plot(self.t,self.z)
               p.ylabel('z')
        elif '=' in s:
            n=s.index('=')
            v=float(s[n+1])
            p.title(s)
            if s[n-1]=='x':
                for i in range(self.N):
                    if i<300000:
                        continue
                    if self.x[i]<v+0.1 and self.x[i]>v-0.1:
                       p.scatter(self.y[i],self.z[i])
                p.xlabel('y')
                p.ylabel('z')
            elif s[n-1]=='y':
                for i in range(self.N):
                    if i<300000:
                        continue
                    if self.y[i]<v+0.1 and self.y[i]>v-0.1:
                       p.scatter(self.x[i],self.z[i])
                p.xlabel('x')
                p.ylabel('z')
            else:
                for i in range(self.N):
                    if i<300000:
                        continue
                    if self.z[i]<v+0.01 and self.z[i]>v-0.01:
                       p.scatter(self.x[i],self.y[i])
                p.xlabel('x')
                p.ylabel('y')
        else:
            if (s[0]== 'x' and s[2]=='y'):
                p.plot(self.x,self.y)
                p.xlabel('x')
                p.ylabel('y')
            elif s[0]=='y' and s[2]=='z':
                p.plot(self.y,self.z)
                p.xlabel('y')
                p.ylabel('z')
            else:
                p.plot(self.x,self.z)
                p.xlabel('x')
                p.ylabel('z')
        p.title(s)
        return None
l=lorenz()
l.__inti__(0,0,100,10,8/3,25,500000,0.0001)
l.caculate()

                
                
                