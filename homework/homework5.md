#Homework5

一、**摘要**
   人口的增减虽然是分离的事件，但是统计上满足微分方程。这也具有一定的合理性，当资源，生产力水平一定时，现有的人口必然影响出生率和死亡率。
然而这样的方程是很难导出的，也是非线性的，本文中将使用数值计算法求解实际人口方程的近似版，以解决一些实际问题。
二、**背景**
   书上第一章1.6题
三、**程序**
import matplotlib.pyplot as pyp #载入需要的包 
T=input('simulating time') #获取数值计算的算法常数
dt=input('steps')
steps=int(T/dt)   #利用获得的数据初始化计算使用的数据
t=[dt*i for i in range(steps)]
N=[None]*steps
N[0]=input('The initial population') #输入初值
a=input('constance one')
b=input('constance two')
for i in range(steps-1): #数值计算
    if N[i]>0:
       N[i+1]=N[i]+dt*(a*N[i]-b*(N[i]**2))
    else:
       N[i+1]=0 
pyp.plot(t,N) #输出图像
pyp.xlabel('time/year')
pyp.ylabel('population/person')
s=str(a/b)
pyp.title('if a/b='+s)

四、**结果**
借助上述程序研究在人口基数为100，步长为0.001，时间为100，b=0.01的情况下不同的出生率下人口变化的规律。
1,a=0.5时：
![picture1](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/50.jpg)
2,a=1
![picture2](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/100.jpg)
3,a=2
![picture3](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/200.jpg)
    
