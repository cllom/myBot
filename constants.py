import numpy as np
from math import pi

timeSteps = 1000
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAnglesFront = np.zeros(1000)
targetAnglesBack = np.zeros(1000)
x = np.linspace(0, 2*pi, 1000)

#amplitude, frequency, and phaseOffset
amplitude = pi/4
frequency = 5 
phaseOffset = 0

maxForce = 20