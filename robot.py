from matplotlib.cbook import file_requires_unicode
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
from sensor import SENSOR
from motor import MOTOR
import constants as c
from math import pi

class ROBOT:
    def __init__(self): 
        self.sensors = {}
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        # create a vector of values to send to the sensor
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Values(t)

    def Prepare_To_Act(self):
        self.motors = {}
        # create a vector of values to send to the motor
        for jointName in pyrosim.jointNamesToIndices:
            f = c.frequency
            if jointName == 'Torso_FrontLeg':
                f *= 1/2
            self.motors[jointName] = MOTOR(jointName,
                                            amplitude=c.amplitude,
                                            frequency=f,
                                            phaseOffset=c.phaseOffset)
    
    def Act(self, t):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId, t)
    
    def Save_Values(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
        for motor in self.motors.values():
            motor.Save_Values()
