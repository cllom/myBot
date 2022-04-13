
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.timeSteps)

        
    def Get_Values(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        """
        if i== self.values.shape[0]-1:
            print(self.linkName)
            print( self.values)
        """
        #c.backLegSensorValues[i]  = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
    
    def Save_Values(self):
        np.save(f'data/{self.linkName}SensorValues.npy', self.values)