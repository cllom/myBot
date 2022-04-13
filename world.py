import pybullet as p
import pybullet_data
import numpy as np

class WORLD:
    def __init__(self):
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")