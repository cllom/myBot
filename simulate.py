import numpy as np
from simulation import SIMULATION
import constants as c

simulation = SIMULATION()
simulation.Run()


"""
np.save('data/backLegSensorValues.npy',c.backLegSensorValues)
np.save('data/frontLegSensorValues.npy',c.frontLegSensorValues)

np.save('data/targetAnglesFront.npy',c.targetAnglesFront)
np.save('data/targetAnglesBack.npy',c.targetAnglesBack)
"""

