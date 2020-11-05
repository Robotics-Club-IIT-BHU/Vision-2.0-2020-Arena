<p align="center">
 <img  width="400" height="400" src="https://github.com/Robotics-Club-IIT-BHU/Vision2_20_Areana/blob/main/media/robo.jpg"><br>
  <i>presents:</i>  
</p>

# Vision 2.0, 2020

Vision 2.0 is an **Image-Processing based Robotics Competition** being organized by the Robotics Club, IIT (BHU), Varanasi to facilitate learning about different components of image processing and its application in building robots capable of autonomous movement.
In this online semester, as all of us are not present physically in the campus, conducting a physical robotics competition was not feasible. Hence, this year the event will be held online using **[PyBullet](https://pybullet.org/) - a python module for physics simulations of robots.**  
This repository holds the **official arena for the event** which will be used for evaluation of the submissions by the participants. The Arena is in the form of an OpenAI gym and **relevant guidelines related to its usage can be found by running [this](https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/helper.py) file.** Run this code from your terminal (make sure the path of the terminal is this repository) and you will see all the helper functions on the terminal window.
<p align="center">
 <img  width="400" height="250" src="https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/media/arena.gif">
 <img  width="400" height="250" src="https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/media/husky.gif"><br>
</p>

## Installation Guidelines

Before installing this arena, you need to download certain modules on which it is dependent. We **strongly** recommend using a distribution of **Linux** as your operating system for this event. Windows installations tend to be a hassle and require, in some instances, quite a bit of time and effort to complete.

0. Although not compulsory, we strongly recommend creating a virtual environment specific to this project. This will help in package management and for decluttering your workspace. A simple way to create a virtual environment is as follows:

   ~~~bash
   python3 -m venv <Env_Name>
   ~~~

   Activation and deactivation of your virtual environment, will be done as specified [here](https://docs.python.org/3/library/venv.html). Scroll down to the table where the activation method for various operating systems is provided. Deactivation, in most cases, can be done by simply typing deactivate while being in in the virtual environment.

1. Once you activate your virtual environment, you will have to install the various dependencies of this project. We have simplified this process for you. Just follow the following steps:
   * Download/Clone this repository on to your local machine.
   * Navigate to the root folder of this repository through your terminal.
   * Execute the following command in your terminal.

      ~~~bash
      pip install -e vision-arena
      ~~~

   * To check whether the installation has been successful, you can refer to our guide/cheatsheet to know how to build the gym in your own python script as well as use the utility functions. You can also check this [file](https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/Arena_Test.py) which shows the implementation of a few functions in the guide.

In case there are problems with the PyBullet installation, you can refer to this [guide](https://github.com/Robotics-Club-IIT-BHU/Robo-Summer-Camp-20/blob/master/Part1/Subpart%201/README.md).

## Using the Arena  

0. You will have to import the package vision_arena, which will be available only if you've completed step 1 in the Installation Guidelines. The arena can be initialized by using:

~~~python
env = gym.make("vision_arena-v0")
~~~

1. Then, you will have to create the working loop, as is normally done in pybullet (using `stepSimulation()`).

2. The functions of the environment, available to you for various purposes, are as follows. Please go through the functions themselves in this [file](https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/vision-arena/vision_arena/envs/vision2arena.py), if you wish to know their arguments and/or return values.
   * `env.camera_feed()`  
      This will return an RGB image of the arena as if a camera was placed on top of the arena.
   * `env.remove_car()`  
      This will be used to remove the car from the arena, in case you want to have a good look at it.
   * `env.respawn_car()`  
      This will be used to respawn the car into the arena, **only after removing it**.
   * `env.roll_dice()`  
      This will simulate the rolling of the dice and will give the next shape and colour to which the car shall have to move.
   * `env.move_husky()`  
      This will be used to give the motor velocity to each wheel individually of the car.
   * `env.reset()`
      This will reset the whole arena. This function cannot be used for your final submission.  
  
 3. You can refer the file **helper.py** to see the documentation of the different functions and **aruco_test.py** to see the detection of aruco marker.
      
## A sample arena from the Camera Feed
<p align="center">
 <img  width="400" height="400" src="https://github.com/Robotics-Club-IIT-BHU/Vision-2.0-2020-Arena/blob/main/media/aruco_detected.png"><br>
</p>

Please note that this image is only indicative, and the arena may be be shuffled.

## Made and maintained by

<table>
   <td align="center">
      <a href="https://github.com/Terabyte17">
         <img src="https://avatars1.githubusercontent.com/u/60649571?s=400&u=e8e56b7d722ad82052f836ca929c79216144e425&v=4" width="100px;" alt=""/>
         <br />
         <sub>
            <b>Yash Sahijwani</b>
         </sub>
      </a>
      <br />
   </td>
   <td align="center">
      <a href="https://github.com/Vikhyath08">
         <img src="https://avatars2.githubusercontent.com/u/55887656?s=460&v=4" width="100px;" alt=""/>
         <br />
         <sub>
            <b>Vikhyath Venkatraman</b>
         </sub>
      </a>
      <br />
   </td>
   <td align="center">
      <a href="https://github.com/Raghav-Soni">
         <img src="https://avatars3.githubusercontent.com/u/60649723?s=460&v=4" width="100px;" alt=""/>
         <br />
         <sub>
            <b>Raghav Soni</b>
         </sub>
      </a>
      <br />
   </td>
</table>
