<p align="center">
 <img  width="400" height="400" src="https://github.com/Robotics-Club-IIT-BHU/Vision2_20_Areana/blob/main/media/robo.jpg"><br>
  <i>presents:</i><br>
</p>

# Vision 2.0, 2020
Vision 2.0 is an **image-processing based robotics competition** being organized by the Robotics Club of IIT (BHU), Varanasi to facilitate learning about different components of image processing and its application in building robots capable of autonomous movement.
In this online semester, as all of us are not present physically in the campus, conducting a physical robotics competition was not feasible. Hence, this year the event will be held online using **PyBullet - a python module for physics simulations of robots.** 
This repository holds the **official arena for the event** which will be used for evaluation of the submissions by the participants. The Arena is in the form of a gym and **relevant guidelines related to its usage can be found [here]().**

## Installation Guidelines
Before installing this arena, you need to download certain modules on which it is dependent. 
The modules are as follows:
1. **gym** <br>
For Windows Users:
~~~
   pip install gym
~~~
2. **OpenCV** <br>
For Windows Users:
~~~
   pip install opencv-python
~~~
3. **PyBullet** <br>
   For installation of PyBullet you can refer this [guide](https://github.com/Robotics-Club-IIT-BHU/Robo-Summer-Camp-20/blob/master/Part1/Subpart%201/README.md).

4. **Numpy** <br>
For Windows Users:
~~~
   pip install numpy
~~~

Once you are over with the installation of all these modules you can proceed to the next step i.e. installing the arena.
To run the arena on your desktop/laptop follow these steps:
1. Download/Clone this repository on to your local machine.
2. Navigate to this repository through your terminal
3. Execute the following command in your terminal
~~~
   pip install -e vision-arena
~~~
4. To check whether the installation has been successful, you can refer our guide/cheatsheet to know how to build the gym in your own python script as well as use the utility functions.
