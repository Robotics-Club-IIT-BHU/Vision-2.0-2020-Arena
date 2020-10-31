import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pybullet as p
import pybullet_data
import cv2
import numpy as np
import random
from os.path import normpath, basename

class VisionArena(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		np.random.seed(0)
		p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-10)
		p.loadURDF('rsc/plane.urdf',[0,0,-0.1], useFixedBase=1)
		p.configureDebugVisualizer(p.COV_ENABLE_WIREFRAME, 0)
		p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)
		
		self.load_arena()
		self.respawn_car()

		self._width = 512
		self._height = 512

	def move_husky(self, leftFrontWheel, rightFrontWheel, leftRearWheel, rightRearWheel):
		self.move(self.husky, leftFrontWheel, rightFrontWheel, leftRearWheel, rightRearWheel)

	def reset(self):
		p.resetSimulation()
		p.setGravity(0,0,-10)
		
		#load arena
		self.husky = p.loadURDF('husky/husky.urdf',[0,0,0],p.getQuaternionFromEuler([0,0,0]))

	def load_arena(self, size = 9):
		'''
		Loading the Arena
		'''
		assert size % 2 == 1, 'Size must be an odd integer'
		
		self.arena = np.random.randint(low = 0, high = 6, size = (size, size))
		# After the arena is updated, the numbers will represent
		# Yellow Square : 6n + 1
		# Yellow Circle : 6n + 2
		# Yellow Triangle : 6n + 3
		# Red Square : 6n + 4
		# Red Circle : 6n + 5
		# Red Triangle : 6n + 6
		# where
		# n = 0 for white base
		# n = 1 for green base
		# n = 2 for blue base
		# n = 3 for cyan base
		# n = 4 for magenta base
		# 31 -> arrow with green base
		# 32 -> arrow with blue base
		# 33 -> arrow with cyan base
		# 34 -> arrow with magenta base
		# 0 -> black
		# -1 -> centre
		shape_colour_dict = {
			0: 'rsc/square/square yellow.urdf',
			1: 'rsc/circle/circle yellow.urdf',
			2: 'rsc/triangle/triangle yellow.urdf',
			3: 'rsc/square/square red.urdf',
			4: 'rsc/circle/circle red.urdf',
			5: 'rsc/triangle/triangle red.urdf',
		}
		self.shape_color = shape_colour_dict
		base_plate_colours = np.random.choice(4, 4, replace = False)
		base_plate_dict = {
			0: 'rsc/base plate/base plate green.urdf',
			1: 'rsc/base plate/base plate blue.urdf',
			2: 'rsc/base plate/base plate cyan.urdf',
			3: 'rsc/base plate/base plate magenta.urdf',
		}
		def get_postion(i, j):
			if self.arena[i, j] % 3 == 2: # If the shape is a triangle
				return [4.2-i*1, 4.2-j*1, 0.03]
			return [4-i*1,4-j*1,0.03]

		for i in range(9):
			for j in range(9):
				if (i==0 or i==8) and j!=4:
						p.loadURDF('rsc/base plate/base plate white.urdf', [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==1 or i==7) and (j==0 or j==8):
						p.loadURDF('rsc/base plate/base plate white.urdf', [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==2 or i==6) and (j!=1 and j!=7 and j!=4):
						p.loadURDF('rsc/base plate/base plate white.urdf', [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==3 or i==5) and (j%2==0 and j!=4):
						p.loadURDF('rsc/base plate/base plate white.urdf', [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==4 and j!=4):
					if j<4:
						p.loadURDF(base_plate_dict[base_plate_colours[0]], [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if j==0:
							p.loadURDF('rsc/arrow/arrow.urdf', [4-i*1,4-j*1,0.03], p.getQuaternionFromEuler([0,0,-np.pi/2]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[0] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[0] + 1) * 6 + self.arena[i, j] + 1
					else:
						p.loadURDF(base_plate_dict[base_plate_colours[1]], [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if j == 8:
							p.loadURDF('rsc/arrow/arrow.urdf', [4-i*1,4-j*1,0.03], p.getQuaternionFromEuler([0,0,np.pi/2]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[1] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[1] + 1) * 6 + self.arena[i, j] + 1
				elif (j == 4 and i != 4):
					if i < 4:
						p.loadURDF(base_plate_dict[base_plate_colours[2]], [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if i == 0:
							p.loadURDF('rsc/arrow/arrow.urdf', [4-i*1,4-j*1,0.03], p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[2] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[2] + 1) * 6 + self.arena[i, j] + 1
					else:
						p.loadURDF(base_plate_dict[base_plate_colours[3]], [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if i == 8:
							p.loadURDF('rsc/arrow/arrow.urdf', [4-i*1,4-j*1,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[3] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[3] + 1) * 6 + self.arena[i, j] + 1
				elif i == 4 and j == 4:
					p.loadURDF('rsc/base plate/base plate white.urdf', [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
					self.arena[i, j] = -1
				else:
					p.loadURDF('rsc/base plate/base plate black.urdf', [4-i*1,4-j*1,0], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
					self.arena[i, j] = 0
		print(self.arena)

	def move(self, car, leftFrontWheel, rightFrontWheel, leftRearWheel, rightRearWheel):
		p.setJointMotorControl2(car,  2, p.VELOCITY_CONTROL, targetVelocity=leftFrontWheel, force=15)
		p.setJointMotorControl2(car,  3, p.VELOCITY_CONTROL, targetVelocity=rightFrontWheel, force=15)
		p.setJointMotorControl2(car,  4, p.VELOCITY_CONTROL, targetVelocity=leftRearWheel, force=15)
		p.setJointMotorControl2(car,  5, p.VELOCITY_CONTROL, targetVelocity=rightRearWheel, force=15)

	def camera_feed(self):
		look = [0, 0, 0.2]
		cameraeyepos = [0, 0, 6.5]
		cameraup = [0, -1, 0]
		self._view_matrix = p.computeViewMatrix(cameraeyepos, look, cameraup)
		fov = 75
		aspect = self._width / self._height
		near = 0.8
		far = 10
		self._proj_matrix = p.computeProjectionMatrixFOV(fov, aspect, near, far)
		img_arr = p.getCameraImage(width=self._width,
                               height=self._height,
                               viewMatrix=self._view_matrix,
                               projectionMatrix=self._proj_matrix,
                               renderer=p.ER_BULLET_HARDWARE_OPENGL)
		rgb = img_arr[2]
		rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
		return rgb

	def remove_car(self):
		p.removeBody(self.husky)

	def respawn_car(self):
		np.random.seed(0)
		pos = [[0,4], [4,0], [8,4], [4,8]]
		ori = [-np.pi/2, 0, np.pi/2, np.pi]
		x = np.random.randint(0,3)
		self.husky = p.loadURDF('husky/husky.urdf', [4-1*pos[x][0],4-1*pos[x][1],0], p.getQuaternionFromEuler([0,0,ori[x]]))

	def roll_dice(self):
		x = random.randint(0,5)
		name = basename(normpath(self.shape_color[x]))
		return name[:-5]