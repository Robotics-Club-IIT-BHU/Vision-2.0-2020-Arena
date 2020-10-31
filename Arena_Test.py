import gym
import vision_arena
import time
import pybullet as p
import pybullet_data
import cv2

if __name__=="__main__":
    env = gym.make("vision_arena-v0")
    for x in range(100):
        p.stepSimulation()
        env.move_husky(0.15, 2, 0.15, 2)
        if x%100==0:
            img = env.camera_feed()
            cv2.imwrite('testrun'+str(x)+'.png', img)
        if x%10==0:
            print(env.roll_dice())
    time.sleep(100)
