import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create('47.100.46.95',4785)

fname = "pos.csv"
f = open(fname, "r")
for line in f.readlines():
    data = line.split(",")
    for cell in data:
        if cell == "clancenter":
            center_x=data[1]
            center_y=data[2]
            center_z=data[3]
        elif cell == "zzm":
            offset_x1=data[1]
            offset_y1=data[2]
            offset_z1=data[3]
        elif cell == "cjm":
            offset_x2=data[1]
            offset_y2=data[2]
            offset_z2=data[3]
        elif cell == "ly":
            offset_x3=data[1]
            offset_y3=data[2]
            offset_z3=data[3]
        elif cell == "fyt":
            offset_x4=data[1]
            offset_y4=data[2]
            offset_z4=data[3]
        elif cell == "zy":
            offset_x5=data[1]
            offset_y5=data[2]
            offset_z5=data[3]
x1=int(center_x)+int(offset_x1)
y1=int(center_y)+int(offset_y1)
z1=int(center_z)+int(offset_z1)
x2=int(center_x)+int(offset_x2)
y2=int(center_y)+int(offset_y2)
z2=int(center_z)+int(offset_z2)
x3=int(center_x)+int(offset_x3)
y3=int(center_y)+int(offset_y3)
z3=int(center_z)+int(offset_z3)
x4=int(center_x)+int(offset_x4)
y4=int(center_y)+int(offset_y4)
z4=int(center_z)+int(offset_z4)
x5=int(center_x)+int(offset_x5)
y5=int(center_y)+int(offset_y5)
z5=int(center_z)+int(offset_z5)
def build(xo=0, yo=0, zo=0, L=10, W=10, H=10, M=1):

    for y in range(H):
        for x in range(L):
            mc.setBlock(xo + x, yo + y, zo, 41)
            mc.setBlock(xo + x, yo + y, zo + W - 1, 41)
        for z in range(W - 2):
            mc.setBlock(xo, yo + y, zo + 1 + z, 41)
            mc.setBlock(xo + L - 1, yo + y, zo + 1 + z, 41)
#....
    for x in range(L):
        for z in range(W):
            mc.setBlock(xo + x, yo, zo + z, M)
            mc.setBlock(xo + x, yo + H - 1, zo + z, 35, 0)
#.......
    for x in range(2):
        for z in range(2):
            mc.setBlock(xo + x + (L - 2) / 2, yo,
                        zo + (W - 2) / 2 + z, 169)
            mc.setBlock(xo + x + (L - 2) / 2, yo + H - 2,
                        zo + (W - 2) / 2 + z, 169)
            mc.setBlock(xo, yo + 4 + x, zo + (W - 2) / 2 + z, 169)

#.
    mc.setBlock(xo + L / 2, yo + 1, zo, 0)
    mc.setBlock(xo + L / 2, yo + 2, zo, 0)
    #..
    for z in range(2):
        for y in range(2):
            mc.setBlock(xo + L - 1, yo + y + 2, zo + (W - 2) / 2 + z,
                        20)




build(x1, y1, z1)
build(x2, y2, z2)
build(x3, y3, z3)
build(x4, y4, z4)
build(x5, y5, z5)

