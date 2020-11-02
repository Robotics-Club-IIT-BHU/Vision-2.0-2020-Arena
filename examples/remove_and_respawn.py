import gym
import vision_arena
import time
import pybullet as p
import pybullet_data
import cv2
import os

if __name__=="__main__":
    parent_path = os.path.dirname(os.getcwd())
    os.chdir(parent_path)
    env = gym.make("vision_arena-v0")
    time.sleep(3)
    env.remove_car()
    time.sleep(3)
    env.respawn_car()
    time.sleep(100)

