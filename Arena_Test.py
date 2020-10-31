import gym
import vision_arena
import time
import pybullet as p
import pybullet_data
import cv2

if __name__=="__main__":
    env = gym.make("vision_arena-v0")
    i=0
    for x in range(100):
        p.stepSimulation()
        env.move_husky(0.15, 2, 0.15, 2)
        print(env.roll_dice())
        if i%100==0:
            img = env.camera_feed()
            cv2.imwrite('testtrun'+str(i)+'.png', img)
        i+=1
    time.sleep(100)
