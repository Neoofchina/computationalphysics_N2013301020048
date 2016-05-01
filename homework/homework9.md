# Homework9
李尧 2013301020048 天眷班
习题3.16
标签（空格分隔）： 混沌 分形 非线性谐振子 
---

**摘要**
    虽然经典力学是确定性的逻辑，牛顿第二定律是确定性的方程，但是确定性的方程也有不确定的解，这些不确定的方程描述的物理现象被称之为混沌。进一步的研究发现，混沌的相空间的吸引子有分形结构。本文将以非线性谐振子为例详细地讨论混动现象。

**背景**
1963年美国气象学家洛伦兹在研究天气的过程中发现了混沌现象。这意味着由于解得不稳定性，即使描述运动的动力学方程是确定的，物理现象仍然不可预测。实际上，混沌现象在我们生活中并不少见，例如湍流。如下图所示
![tuanliu](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/tuanliu.jpg)
简单的烟雾从喷嘴喷出后，先是可预测的层流，然后是完全无法预测的湍流。人们在研究混沌的过程中发现了混沌与分形的联系，简单地说，混沌的吸引子具有分形的特征，即自相似。实际上，混沌可以说是时空间的分形，分形可以说是空间的混沌。如烟雾中的大涡旋里套着小涡旋，小涡旋套着更小的涡旋。

**物理模型与计算方法**
考虑一个受到驱动和摩擦的物理摆，他的运动方程由下式给出：
$\frac{d^2x}{dt^2}=-\frac{g}{l}sin(\theta)-g\frac{d\theta}{dt}+F_Dsin(\Omega_Dt)$
我们把这个一元二阶常微分方程变成等价的二元一阶常微分方程组：
$\frac{d\omega}{dt}=-\frac{g}{l}sin(\theta)-g\omega+F_Dsin(\Omega_Dt)$
$\frac{d\theta}{dt}=\omega$
这个方程组是不可解析求解的，但是可以用Euler-Cromer方法数值求解。这样我实际上使用的是以下的迭代关系式：
$\omega_{i+1}=\omega_i+\Delta t*（-\frac{g}{l}sin(\theta_{i+1})-g\omega_{i}+F_Dsin(\Omega_Dt)）$
$\theta_{i+1}=\theta_{i}+\Delta t*\omega_{i+1}$

根据以上的分析，模拟实验的代码如下：
[program](https://github.com/Neoofchina/computationalphysics_N2013301020048/blob/master/program/chaos.py)

**解的稳定性分析**
我们设满足上式的解为。
$\theta_{i}$
$\omega_i$
现在考虑在解附近有微小的$\delta$的偏离，由于$\delta$很小，我们可以只保留一阶项。方程改写为
$\delta\omega_{i+1}=\delta\omega_i+\Delta t*(-\frac{g}{l}cos(\theta)\delta\omega_i-g\delta\omega_{i})$
