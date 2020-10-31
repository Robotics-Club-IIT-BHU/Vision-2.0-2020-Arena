import gym 
import pybullet as p
import pybullet_data
import vision_arena
import time

if __name__=="__main__":
    env = gym.make("vision_arena-v0")
    
    print(env.move_husky.__doc__)
    print(env.reset.__doc__)
    print(env.camera_feed.__doc__)
    print(env.remove_car.__doc__)
    print(env.respawn_car.__doc__)
    print(env.roll_dice.__doc__)



