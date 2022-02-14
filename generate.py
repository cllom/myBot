import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

l = 1
w = 1
h = 1
z_pos = 0.5
x_pos = 0
y_pos = 0
for y in range(3):
    for x in range(3):
        for z in range(10):
            pyrosim.Send_Cube(name="Box"+str(z), pos=[x_pos,y_pos,z_pos] , size=[l,w,h])
            z_pos += 1.2
            l *= 0.8
            w *= 0.8
            h *= 0.8
        x_pos += 1
        z_pos = 0.5
        l = 1
        w = 1
        h = 1
    x_pos = 0
    y_pos += 1
    z_pos = 0.5
    l = 1
    w = 1
    h = 1

pyrosim.End()