import gym 
import pybullet as p
import pybullet_data
import vision_arena
import time

if __name__=="__main__":
    env = gym.make("vision_arena-v0")
    
    print("move_husky function--")
    print(env.move_husky.__doc__)

    print("reset_function--")
    print(env.reset.__doc__)

    print("camera_feed_function--")
    print(env.camera_feed.__doc__)

    print("remove_car_function--")
    print(env.remove_car.__doc__)
    
    print("respawn_car_function--")
    print(env.respawn_car.__doc__)

    print("roll_dice_function--")
    print(env.roll_dice.__doc__)



