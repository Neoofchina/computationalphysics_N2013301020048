#***Homewoork7***
**Abstract**

To study the motion of a batted ball in air, we simulate it with Eular method based on the known classical princple, where we supposed the air
density , the wind and the gravity  are constant. The result shows how the ball and the air interact with each other and creat odd orbits

**Background** 

Baseball is a very popular sport in the US now, and there are so many skills to creat odd orbits, such as fast ball, curve ball and kunckleball. Some similar cases happen in bing-bong ball.  A good athlete only need to know how to do these, but physicists more concern on why the motion of those ball  are so strange? These balls can be simpled as a batted ball to study and simulated by conputers.

**Force**

To simulate the motion of a batted ball, we must firstly analyze what forces will apply on the batted ball. The gravity, the air resistance, the wind
force and the  pressure difference due to spin are the major forces need to be taken into account. And in the air-rest-frame, the air resistance and the wind force can be unified to one force which we refer as air-drag-force. 
  
  Then according to the Bernouli's theory[1], the pressure difference is propotional to the spin velocity and the velocity in the air-rest-frame, and the director is prependicular to spin velocity and   the velocity in the air-rest-frame. In a nutshell, this force must equal to the cross mutiplication of
 the spin velocity and the velocity in the air-rest-frame.

**Program**

[code](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/program/baseball.py)

It's convenical to do vector algebraic in three dimensional world, so that after initiating the program by reading some parameters, I defined some functions to do vector algebraic. But no all of them, we just need cross mutipication and vector-addition. Then the Eular method to solve a set of partial equations is following. At the end of the codes, I use 'Marplotlib' draw 2-D diagram. In addition, all 3-D diagram are drawn by Matlab using the result of this program.

**Result**

As the problem 2.19 argues, we first consider a back spin batted ball in air and the spin velocity is 2000rpm. So I set three case: back spin 2000rpm, forward spin 2000rpm and no spin, and spins are perpendicular to the velocity. These are  2-D cases and the result is given by picture1.

picture1:

![picture1](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/Z_OSDZ%5DI%40AP4%7DJY_X%245VGB8.png)
As picture1 shows, a  ball with back spin 2000rpm will be lift by the pressure difference due to spin and not likes golf, this force is too strong to help the ball to go  farther.

We also considered some general cases, where spin and velocity are no prependicular to each other, and those orbits are very odd. A example is given by picture2.

picture2:
![picture2](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/baseball1%2B.jpg)

If there is no spin, the orbit is given by picture3.

picture3:
![picture3](https://raw.githubusercontent.com/Neoofchina/computationalphysics_N2013301020048/master/picture/baseball2.jpg)

In consequence, the couple of spin and velocity in air rest frame affect the orbit of the batted ball a lot, if there is no spin or no Bernouli's theory, those games will be boring.