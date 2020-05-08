import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create('47.100.46.95',4785)
#entityId2 = mc.getPlayerEntityId("zhuzhe")

#pos=mc.entity.getPos(entityId2)

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
            offset_x=data[1]
            offset_y=data[2]
            offset_z=data[3]
x=int(center_x)+int(offset_x)+13
y=int(center_y)+int(offset_y)
z=int(center_z)+int(offset_z)

mc.setBlocks(x,y,z,x+9,y+9,z+9,41)
mc.setBlocks(x+1,y+1,z+1,x+8,y+8,z+8,0)
