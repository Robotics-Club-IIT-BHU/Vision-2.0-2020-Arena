import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pybullet as p
import pybullet_data
import cv2
import numpy as np

class VisionArena(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-10)
    p.loadURDF('rsc/plane.urdf',[0,0,-0.1], useFixedBase=1)
    p.configureDebugVisualizer(p.COV_ENABLE_WIREFRAME, 0)
    p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)
    
    self.load_arena()
    self.husky = p.loadURDF('husky/husky.urdf',[0,0,0.1],p.getQuaternionFromEuler([0,0,0]))

  def move_husky(self, leftFrontWheel, rightFrontWheel, leftRearWheel, RighRearWheel):
    self.move(self.husky, leftFrontWheel, rightFrontWheel, leftRearWheel, RighRearWheel)

  def reset(self):
    p.resetSimulation()
    p.setGravity(0,0,-10)
    
    #load arena
    self.husky = p.loadURDF('husky/husky.urdf',[0,0,0],p.getQuaternionFromEuler([0,0,0]))

  def load_arena(self):
      for i in range(9):
          for j in range(9):
              if (i==0 or i==8) and j!=4:
                 p.loadURDF('rsc/base plate/base plate white.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/square/square yellow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
              #normal squares
              elif (i==1 or i==7) and (j==0 or j==8):
                 p.loadURDF('rsc/base plate/base plate white.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/triangle/triangle red.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,-np.pi/4]), useFixedBase=1)
              #normal squares
              elif (i==2 or i==6) and (j!=1 and j!=7 and j!=4):
                 p.loadURDF('rsc/base plate/base plate white.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/circle/circle yellow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #normal squares
              elif (i==3 or i==5) and (j%2==0 and j!=4):
                 p.loadURDF('rsc/base plate/base plate white.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/circle/circle red.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)              
              #normal squares
              elif (i==4 and j!=4):
                 if j<4:
                     p.loadURDF('rsc/base plate/base plate green.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 else:
                     p.loadURDF('rsc/base plate/base plate blue.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 if (j==0 or j==8):
                     if j==0:
                        p.loadURDF('rsc/arrow/arrow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,-np.pi/2]), useFixedBase=1)
                     else:
                        p.loadURDF('rsc/arrow/arrow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,np.pi/2]), useFixedBase=1)
                 else:
                     p.loadURDF('rsc/square/square red.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #colored paths
              elif i==0 and j==4:
                 p.loadURDF('rsc/base plate/base plate cyan.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/arrow/arrow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
               #arrow
              elif i==8 and j==4:
                 p.loadURDF('rsc/base plate/base plate magenta.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/arrow/arrow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #arrow
              elif i<4 and j==4:
                 p.loadURDF('rsc/base plate/base plate cyan.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/triangle/triangle yellow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #colored paths
              elif i>4 and j==4:
                 p.loadURDF('rsc/base plate/base plate magenta.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/circle/circle yellow.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #colored paths
              elif j==4:
                 p.loadURDF('rsc/base plate/base plate white.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
                 p.loadURDF('rsc/circle/circle red.urdf', [3-i*0.75,3-j*0.75,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #centre block
              else:
                 p.loadURDF('rsc/base plate/base plate black.urdf', [3-i*0.75,3-j*0.75,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
              #black boxes

  def move(self, car, leftFrontWheel, rightFrontWheel, leftRearWheel, RighRearWheel):
      p.setJointMotorControl2(car,  2, p.VELOCITY_CONTROL, targetVelocity=leftFrontWheel, force=15)
      p.setJointMotorControl2(car,  3, p.VELOCITY_CONTROL, targetVelocity=rightFrontWheel, force=15)
      p.setJointMotorControl2(car,  4, p.VELOCITY_CONTROL, targetVelocity=leftRearWheel, force=15)
      p.setJointMotorControl2(car,  5, p.VELOCITY_CONTROL, targetVelocity=rightRearWheel, force=15)
