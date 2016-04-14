#**Homework**

**Abstact:**

In this paper, we aim to use computer to find out the relation between amplitude and period of nonlinear pendulum.

**Background**

In history, because it's impossible to find the accurate solutions of nonlinear partial differential equations , to study the pendulum, scientists prefered to use the small angle limit to linearize the original partial differential equation. Even through this was a unperfect work,  many achievements were made, likes the pendulum clock. But now, we can study more on pendulum by computers. 

**Program**

![code](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/program/nonlinearpendulum.py)

Firstly, we need to design a function to caculate the motion of the pendulum we study. And the pendulum goes back and forth, if the eror of 
numerical caculation is still positive or negative, this simulation must be further and further from the real situation. Such that we choose Euler-Cromer method but Euler method to do this caculation. And there is a small
trick in our function, where program will draw the result or not based on input. 

Then, we should measure the period of our results. It's unrealistic to do this work by eyes or putting a rule on the screen, so we define another function to judge whether the inputted points are peaks or gaps. In fact, we just label the positions but don't distinguish peaks and gaps, which is aim to increase the amount of samples.

The above two process are finished in only one cycle to decrease the time that the whole program will taking. According to our results, we can use a few codes to find out the periods. Attention! We take the average of periods as our measure result, because of  errors.

Finally, we can define a cycle where we caculate the periods of  a number of amplitude from 0 to pi/2 and plot a line to show the relation between amplitude and period of pendulum.

**Consequence**

In the program, we suppose that the gravity constance g=9.8m/s^2, and the length of our pendulum is 1 meter. The period in small angle limit is around 2.02s.To test the period will vary with the amplitude, we first let the amplitudes be pi/10, pi/3 and pi/2. 

![picture1](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/A.png)

The above picture shows the period exactly vary with the amplitude and our work is meaningful.

The next step is find out the relation between the period and the amplitude. And the result given by our program is following.

![picture2](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/T-A.png)

As theory had predicted, the period is almost 2.01s when the amplitude is small, which is very close too 2.02s. 






