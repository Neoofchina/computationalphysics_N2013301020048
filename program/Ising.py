# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 20:37:12 2016

@author: 李尧
"""
#导入需要使用的程序包
from math import *
import matplotlib.pyplot as p
import numpy.random as ran
#建立计算Ising模型的类
class Ising():
    def __inti__(self,J,N,T,istate):#初始化
        self.N=N
        self.T=T
        self.J=-J
        self.state=istate
        self.B=[0 for i in range(N)]
        self.Interactionmatrics=[[0 for i in range(N)] for i in range(N)]
        return None
    def setinteractionmatrics(self,newmatric):#设置相互作用矩阵或关联矩阵
        self.Interactionmatrics=newmatric
        return None
    def setB(self,B):#设置磁场
        for i in range(self.N):
            self.B[i]=-B
        return None
    def setT(self,T):#设置温度
        self.T=T
        return None
    def energy(self):#计算总能量
        E=0
        for i in range(self.N):
            for j in range(self.N):
                if self.state[i]==0 or self.Interactionmatrics[i][j]==0 or self.state[j]==0:
                    continue
                E=E+self.state[i]*self.Interactionmatrics[i][j]*self.state[j]*self.J*0.5
            if self.B[i]==0:
                continue
            else:
                E=E+self.B[i]*self.state[i]
        return E
    def M(self):#计算总磁矩
        M=0        
        for i in range(N):
           M=self.state[i]+M
        return M
    def sweep(self):#一次演化
        for i in range(self.N):
            E1=self.nearbyinteraction(i)
            self.state[i]=0-self.state[i]
            E2=self.nearbyinteraction(i)
            e=E1-E2
            if e <0:
               p=exp(e/self.T)
               r=ran.random()
               if r>p: 
                   self.state[i]=0-self.state[i]
        return None
    def nearbyinteraction(self,x):#计算近邻或次近邻原子间的相互作用能
        e=0
        for i in range(self.N):
            if self.Interactionmatrics[x][i]==0 or self.state[i]==0:
                continue
            e=e+self.state[x]*self.Interactionmatrics[x][i]*self.state[i]*self.J
        if self.B[x]!=0:
            e=e+self.B[x]*self.state[x]
        return e
#起辅助功能的函数
def oneton(x,n,k):#一维坐标到n为坐标的变化
    y=[]
    for i in range(k):
        y.append(int(x/n**(k-1-i)))
        x=x-y[-1]*n**(k-1-i)
    return y
def ntoone(y,n,k):#n维坐标到一维坐标的变换
    x=0
    for i in range(k):
       x=x+n**(k-1-i)*y[i]
    return x
def R(x,n):#周期性边界条件修正函数
    if x>n/2:
        return n-x
    else:
        return x
def isnear(y1,y2,n):#计算距离
    k=len(y1)
    y=[R(abs(y1[i]-y2[i]),n) for i in range(k)]
    d=0
    for i in range(k):
        d=y[i]+d
    return d
def standarymetrics(n,k):#生成n维正方格子的关联矩阵或相互作用矩阵
    N=n**k
    metric=[[0 for i in range(N)] for i in range(N)]
    for x in range(N):
        for y in range(N):
            d=isnear(oneton(x,n,k),oneton(y,n,k),n)
            if d==1:
                metric[x][y]=1.0
            if d==2:#只记最近邻了略去
                metric[x][y]=0.35
    return  metric
def ave(x):#计算平均值
    l=len(x)
    X=0
    for i in range(l):
        X=X+x[i]
    avex=X/l
    return avex
#计算磁滞回线的主程序
line=Ising()
n=input('n=')
k=input('k=')
N=n**k
istate=[1.0 for i in range(N)]
line.__inti__(1.0,N,2,istate)  
metric=standarymetrics(n,k)
line.setinteractionmatrics(metric)
B=[-5.0+0.4*i for i  in range(25)]
t=[ i for i in range(1000)]
a1=[]
a2=[]
M=[]
T=[0.5*i+1.0 for i in range(30)]
for j in range(50):
  if j<25:
    line.setB(B[j])
    M=[]
    for i in range(1000):
       M.append(line.M())
       line.sweep()
    a1.append(ave(M))
  else:
     line.setB(B[24-j])
     M=[]
     for i in range(1000):
        M.append(line.M())
        line.sweep()
     a2.append(ave(M))
a2.reverse()
p.plot(B,a1,B,a2)
p.ylim(-130,130) 
p.xlabel('B')
p.ylabel('M')  
p.title('3-D Ising mode and hysteresis loop') 


#计算铁磁相变的主程序
line=Ising()
n=input('n=')
k=input('k=')
N=n**k
istate=[1.0 for i in range(N)]
line.__inti__(1.0,N,2,istate)  
metric=standarymetrics(n,k)
line.setinteractionmatrics(metric)
B=[-5.0+0.4*i for i  in range(25)]
t=[ i for i in range(1000)]
a1=[]
a2=[]
M=[]
T=[0.5*i+1.0 for i in range(30)]
for j in range(30):
  line.setT(T[j])
  M=[]
  for i in range(1000):
      M.append(line.M())
      line.sweep()
  a.append(ave(M))
print(a)
p.ylim(-120,120)
p.plot(T,a) 
p.xlabel('T')
p.ylabel('M')  
p.title('1-D Ising mode and phase transition')#根据需要更改    