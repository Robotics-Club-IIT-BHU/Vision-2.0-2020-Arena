import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pybullet as p
import pybullet_data
import cv2

class VisionArena(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())


  def step(self, action):
    pass

  def reset(self):
    pass

  def render(self, mode='human', close=False):
    pass

