from cmath import phase
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self, 
                jointName,
                amplitude,
                frequency,
                phaseOffset):
        self.jointName = jointName
        self.amplitude = amplitude
        self.frequency = frequency
        self.phaseOffset = phaseOffset

        self.motorValues = amplitude * np.sin(frequency 
                                        * np.linspace(0, 2*np.pi, c.timeSteps)
                                        + phaseOffset)

    def Set_Value(self, robot_id, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot_id,
                        jointName=self.jointName,
                        controlMode=p.POSITION_CONTROL,
                        targetPosition=self.motorValues[t],
                        maxForce=c.maxForce)

    def Save_Values(self):
        np.save(f'data/{self.jointName}MotorsValues.npy', self.motorValues)