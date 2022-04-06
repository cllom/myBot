from math import pi
from re import A
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAnglesFront = np.zeros(1000)
targetAnglesBack = np.zeros(1000)
x = np.linspace(0, 2*pi, 1000)

#amplitude, frequency, and phaseOffset
FrontLeg = np.array([pi/4, 5, 0])
BackLeg = np.array([pi/4, 5, pi/4])


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i]  = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
    frontLegSensorValues[i]  = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    targetAnglesFront[i] = FrontLeg[0] * np.sin(FrontLeg[1] * x[i] + FrontLeg[2])  
    targetAnglesBack[i] = BackLeg[0] * np.sin(BackLeg[1] * x[i] + BackLeg[2])  


    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = "BackLeg_Torso",

    controlMode = p.POSITION_CONTROL,

    targetPosition = -targetAnglesFront[i],

    maxForce = 20)
    
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = "Torso_FrontLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = targetAnglesBack[i],

    maxForce = 20) 

    time.sleep( 1/240 )


np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)

np.save('data/targetAnglesFront.npy',targetAnglesFront)
np.save('data/targetAnglesBack.npy',targetAnglesBack)

p.disconnect()
