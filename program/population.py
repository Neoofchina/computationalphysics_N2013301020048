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
