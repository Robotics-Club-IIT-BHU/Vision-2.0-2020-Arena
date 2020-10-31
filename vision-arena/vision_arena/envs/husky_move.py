import pybullet as p
import pybullet_data

def move(self, car, leftFrontWheel, rightFrontWheel, leftRearWheel, RighRearWheel):
    p.setJointMotorControl2(car,  2, p.VELOCITY_CONTROL, targetVelocity=leftFrontWheel, force=15)
    p.setJointMotorControl2(car,  3, p.VELOCITY_CONTROL, targetVelocity=rightFrontWheel, force=15)
    p.setJointMotorControl2(car,  4, p.VELOCITY_CONTROL, targetVelocity=leftRearWheel, force=15)
    p.setJointMotorControl2(car,  5, p.VELOCITY_CONTROL, targetVelocity=rightRearWheel, force=15)
