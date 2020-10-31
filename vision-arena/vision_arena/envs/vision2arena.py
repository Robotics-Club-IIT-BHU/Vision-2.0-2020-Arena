import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pybullet as p
import pybullet_data
import cv2
from husky_move import move

class VisionArena(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-10)
    
    self.load_arena()
    self.husky = p.loadURDF('husky/husky.urdf',[0,0,0],p.getQuaternionFromEuler([0,0,0]))

  def move_husky(self, leftFrontWheel, rightFrontWheel, leftRearWheel, RighRearWheel):
    move(self.husky, leftFrontWheel, rightFrontWheel, leftRearWheel, RighRearWheel)

  def reset(self):
    p.resetSimulation()
    p.setGravity(0,0,-10)
    
    #load arena
    self.husky = p.loadURDF('husky/husky.urdf',[0,0,0],p.getQuaternionFromEuler([0,0,0]))

  def load_arena(self):
      for i in range(9):
          for j in range(9):
              if (i==0 or i==8) and j!=4:
                  pass
              #normal squares
              elif (i==1 or i==7) and (j==0 or j==8):
                  pass
              #normal squares
              elif (i==2 or i==6) and (j!=1 and j!=7 and j!=4):
                  pass
              #normal squares
              elif (i==3 or i==5) and (j%2==0 and j!=4):
                  pass
              #normal squares
              elif (i==4 and j!=4):
                  pass
              #colored paths
              elif i==0 and j==4:
                  pass
               #arrow
              elif i<4 and j==4:
                  pass
              #colored paths
              elif i>4 and j==4:
                  pass
              #colored paths
              elif j==4:
                  pass
              #centre block
              else:
                  pass
              #black boxes

