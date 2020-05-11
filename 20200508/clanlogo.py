import binvox_rw
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
        elif cell == "clanlogo":
            offset_x1=data[1]
            offset_y1=data[2]
            offset_z1=data[3]
x1=int(center_x)+int(offset_x1)
y1=int(center_y)+int(offset_y1)
z1=int(center_z)+int(offset_z1)
with open('clanlogo.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
#print(model.data)

for y in range(model.dims[1]):
    print("layer y=",y)
    layer_data=model.data[y]
    stringlayer=""
    for x in range(model.dims[0]):
        stringlayer=stringlayer+"\n"
        for z in range(model.dims[2]):
            if model.data[x][y][z] == True:
                stringlayer=stringlayer+'1'
                mc.setBlock(x1+x,y1+y,z1+z,138)
            else:
                stringlayer=stringlayer+'0'
                mc.setBlock(x1+x,y1+y,z1+z,0)
    print(stringlayer)
