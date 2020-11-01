import gym
import vision_arena
import time
import pybullet as p
import pybullet_data
import cv2

if __name__=="__main__":
    env = gym.make("vision_arena-v0")
    x=0
    while True:
        p.stepSimulation()
        env.move_husky(5, 5, 5, 5)
        if x==20:
            img = env.camera_feed()
            cv2.imwrite('media/testrun'+str(x)+'.png', img)
        x+=1
    time.sleep(100)