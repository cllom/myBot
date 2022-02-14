import pyrosim.pyrosim as pyrosim



l = 1
w = 1
h = 1

x_pos = 0
y_pos = 0
z_pos = 0.5*h


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x_pos+5,y_pos+5,z_pos] , size=[l,w,h])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="BackLeg", pos=[0,0,0.5] , size=[l,w,h])
    pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="Torso", pos=[0.5,0,0.5] , size=[l,w,h])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[l,w,h])
    pyrosim.End()

Create_World()
Create_Robot()