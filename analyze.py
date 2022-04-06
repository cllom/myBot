import numpy 
import matplotlib.pyplot


"""
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/FrontLegSensorValues.npy')
matplotlib.pyplot.plot(backLegSensorValues, label = "torso leg")
matplotlib.pyplot.plot(frontLegSensorValues, label = "front leg")
"""

targetAnglesFront = numpy.load('data/targetAnglesFront.npy')
targetAnglesBack = numpy.load('data/targetAnglesBack.npy')
matplotlib.pyplot.plot(targetAnglesFront, label = "targetAnglesFront")
matplotlib.pyplot.plot(targetAnglesBack, label = "targetAnglesBack")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()