<p align="center">
 <img  width="400" height="400" src="https://github.com/Robotics-Club-IIT-BHU/Vision2_20_Areana/blob/main/media/robo.jpg"><br>
  <i>presents:</i>  
</p>

# Vision 2.0, 2020

Vision 2.0 is an **Image-Processing based Robotics Competition** being organized by the Robotics Club, IIT (BHU), Varanasi to facilitate learning about different components of image processing and its application in building robots capable of autonomous movement.
In this online semester, as all of us are not present physically in the campus, conducting a physical robotics competition was not feasible. Hence, this year the event will be held online using **[PyBullet](https://pybullet.org/) - a python module for physics simulations of robots.**  
This repository holds the **official arena for the event** which will be used for evaluation of the submissions by the participants. The Arena is in the form of an OpenAI gym and **relevant guidelines related to its usage can be found [here]().**

## Installation Guidelines

Before installing this arena, you need to download certain modules on which it is dependent. We **strongly** recommend using a distribution of **Linux** as your operating system for this event. Windows installations tend to be a hassle and require, in some instances, quite a bit of time and effort to complete.

0. Although not compulsory, we strongly recommend creating a virtual environment specific to this project. This will help in package management and for decluttering your workspace. A simple way to create a virtual environment is as follows:

   ~~~bash
   pip3 install venv
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

   * To check whether the installation has been successful, you can refer to our guide/cheatsheet to know how to build the gym in your own python script as well as use the utility functions.

In case there are problems with the PyBullet installation, you can refer to this [guide](https://github.com/Robotics-Club-IIT-BHU/Robo-Summer-Camp-20/blob/master/Part1/Subpart%201/README.md).
