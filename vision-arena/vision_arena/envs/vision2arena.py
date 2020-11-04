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
		"""Constructor Function.

		Function to initialize and load the Arena
		List of Functions:
			
			move_husky
			reset
			camera_feed
			remove_car
			respawn_car
			roll_dice

		No Arguments
		"""

		p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.setGravity(0,0,-15)
		p.loadURDF('rsc/plane.urdf',[0,0,-0.1], useFixedBase=1)
		p.configureDebugVisualizer(p.COV_ENABLE_WIREFRAME, 0)
		p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)
		

		self.husky = None

		self.__load_arena()
		self.respawn_car()

		self._width = 512
		self._height = 512

	def move_husky(self, leftFrontWheel, rightFrontWheel, leftRearWheel, rightRearWheel):
		"""
		Function to give Velocities to the wheels of the robot.
			
		Arguments:

			leftFrontWheel - Velocity of the front left wheel  
			rightFrontWheel - Velocity of the front right wheel  
			leftRearWheel - Velocity of the rear left wheel  
			rightRearWheel - Velocity of the rear right wheel  


		Return Values:

			None
		"""

		self.__move(self.husky, leftFrontWheel, rightFrontWheel, leftRearWheel, rightRearWheel)

	def reset(self):
		"""
		Function to restart the simulation.

		This will undo all the previous simulation commands and the \
		arena along with the robot will be loaded again.
		
		Only for testing purposes. Won't be used in final evaluation.

		Arguments:

			None

		Return Values:

			None
		"""
		np.random.seed(0)
		p.resetSimulation()
		p.setGravity(0,0,-10)

		p.loadURDF('rsc/plane.urdf',[0,0,-0.1], useFixedBase=1)
		p.configureDebugVisualizer(p.COV_ENABLE_WIREFRAME, 0)
		p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)
		
		self.__load_arena()
		self.respawn_car()

	def __load_arena(self):
		"""
		Function to load the arena
		"""
		
		self.arena = np.random.randint(low = 0, high = 6, size=(9, 9))
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
				return [4.1-i*1, 4-j*1, 0.03]
			return [4-i*1,4-j*1,0.03]
		
		def get_base_plate_position(i, j):
			return [4-i*1,4-j*1,0]

		for i in range(9):
			for j in range(9):
				if (i==0 or i==8) and j!=4:
						p.loadURDF('rsc/base plate/base plate white.urdf', get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==1 or i==7) and (j==0 or j==8):
						p.loadURDF('rsc/base plate/base plate white.urdf', get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==2 or i==6) and (j!=1 and j!=7 and j!=4):
						p.loadURDF('rsc/base plate/base plate white.urdf', get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==3 or i==5) and (j%2==0 and j!=4):
						p.loadURDF('rsc/base plate/base plate white.urdf', get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
						self.arena[i, j] = self.arena[i, j] + 1
				elif (i==4 and j!=4):
					if j<4:
						p.loadURDF(base_plate_dict[base_plate_colours[0]], get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if j==0:
							p.loadURDF('rsc/arrow/arrow.urdf', [4.1-i*1,4-j*1,0.03], p.getQuaternionFromEuler([0,0,-np.pi/2]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[0] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[0] + 1) * 6 + self.arena[i, j] + 1
					else:
						p.loadURDF(base_plate_dict[base_plate_colours[1]], get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if j == 8:
							p.loadURDF('rsc/arrow/arrow.urdf', [3.9-i*1,4-j*1,0.03], p.getQuaternionFromEuler([0,0,np.pi/2]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[1] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[1] + 1) * 6 + self.arena[i, j] + 1
				elif (j == 4 and i != 4):
					if i < 4:
						p.loadURDF(base_plate_dict[base_plate_colours[2]], get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if i == 0:
							p.loadURDF('rsc/arrow/arrow.urdf', [4-i*1,3.9-j*1,0.03], p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[2] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[2] + 1) * 6 + self.arena[i, j] + 1
					else:
						p.loadURDF(base_plate_dict[base_plate_colours[3]], get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
						if i == 8:
							p.loadURDF('rsc/arrow/arrow.urdf', [4-i*1,4.1-j*1,0.03], p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
							self.arena[i, j] = base_plate_colours[3] + 31
						else:
							p.loadURDF(shape_colour_dict[self.arena[i, j]], get_postion(i, j), p.getQuaternionFromEuler([0,0,np.pi]), useFixedBase=1)
							self.arena[i, j] = (base_plate_colours[3] + 1) * 6 + self.arena[i, j] + 1
				elif i == 4 and j == 4:
					p.loadURDF('rsc/base plate/base plate white.urdf', get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
					self.arena[i, j] = -1
				else:
					p.loadURDF('rsc/base plate/base plate black.urdf', get_base_plate_position(i, j), p.getQuaternionFromEuler([0,0,0]), useFixedBase=1)
					self.arena[i, j] = 0

	def __move(self, car, leftFrontWheel, rightFrontWheel, leftRearWheel, rightRearWheel):
		p.setJointMotorControl2(car,  4, p.VELOCITY_CONTROL, targetVelocity=leftFrontWheel, force=30)
		p.setJointMotorControl2(car,  5, p.VELOCITY_CONTROL, targetVelocity=rightFrontWheel, force=30)
		p.setJointMotorControl2(car,  6, p.VELOCITY_CONTROL, targetVelocity=leftRearWheel, force=30)
		p.setJointMotorControl2(car,  7, p.VELOCITY_CONTROL, targetVelocity=rightRearWheel, force=30)

	def camera_feed(self, is_flat = False):
		"""
		Function to get camera feed of the arena.

		Arguments:

			None
		
		Return Values:

			numpy array of RGB values
		"""
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
		if is_flat == True:
			# Only for those who are getting a blank image in opencv
			rgb = np.array(rgb)
			rgb = np.reshape(rgb, (512, 512, 4))
		rgb = np.uint8(rgb)
		rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
		return rgb

	def remove_car(self):
		"""
		Function to remove the car from the arena.

		Arguments:

			None

		Return Values:

			None
		"""
		p.removeBody(self.husky)
		self.husky = None

	def respawn_car(self):
		"""
		Function to respawn the car from the arena.

		Arguments:

			None

		Return Values:

			None
		"""
		if self.husky is not None:
			print("Old Car being Removed")
			p.removeBody(self.husky)
			self.husky = None

		pos = [[0,4], [4,0], [8,4], [4,8]]
		ori = [-np.pi/2, 0, np.pi/2, np.pi]
		x = np.random.randint(0,3)
		self.husky = p.loadURDF('rsc/car/car.urdf', [4-1*pos[x][0],4-1*pos[x][1],0], p.getQuaternionFromEuler([0,0,ori[x]]))
		#self.husky = p.loadURDF('husky/husky.urdf', [4-1*pos[x][0],4-1*pos[x][1],0], p.getQuaternionFromEuler([0,0,ori[x]]))
		#self.aruco = p.loadURDF('rsc/aruco/aruco.urdf', [4-1*pos[x][0],4-1*pos[x][1],1.2], p.getQuaternionFromEuler([1.5707,0,ori[x]]))
		#p.createConstraint(self.husky, -1, self.aruco, -1, p.JOINT_FIXED, [0,0,1], [0,0,0.4], [0,0,0], childFrameOrientation = p.getQuaternionFromEuler([0,0,1]))
		for x in range(100):
			p.stepSimulation()

	def roll_dice(self):
		"""
		Function imitating a ludo dice.
		
		This function gives the next shape and color to move to in the arena.
		
		Arguments:

			None

		Return Values:

			A string of one of the following:

				CY - (circle yellow)  
				TY - (triangle yellow)  
				SY - (square yellow)    
				CR - (circle red)
				TR - (triangle red)  
				SR - (square red)
		"""

		x = random.randint(0,5)
		name = basename(normpath(self.shape_color[x]))
		code_list = name[:-5].split(' ')
		code = code_list[0][0].capitalize() + code_list[1][0].capitalize()
		return code
