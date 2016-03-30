import matplotlib.pyplot as pyp

T=input('模拟的反应时间')

dt=input('数值模拟的步长')

N=int(T/dt)

t=[i*dt for i in range(N)]

na=[None]*N

nb=[None]*N    //根据获取的数据初始化计算过程中使用的数组（列表），常数等

na[0]=input('A的初始原子数')

ta=input('A的衰变常数')

nb[0]=input('B的初始原子数')

tb=input('B的衰变常数')//通过人机交互获取模拟的初始数据

for i in range(N-1):
  
  na[i+1]=na[i]-dt*na[i]/ta
  
  nb[i+1]=nb[i]-dt*nb[i]/tb+dt*na[i]/ta//用欧勒法数值解微分方程组

pyp.plot(t,na,'k',t,nb,'r')

pyp.title('NA='+na[0]+'  Ta='+ta+'NB='+nb[0]+'  Tb='+tb)

pyp.xlable('时间/年')

pyp.ylable('粒子数/个')//绘图
