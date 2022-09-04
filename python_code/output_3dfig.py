from pygadgetreader import readrockstar
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_dirB = "/home/jun/work_place/astrophysics_project/rockstar-master/dataB_result/"
_file = "halos_0"

pos_arr = readrockstar(_dir+_file,"pos")
pos_arrB = readrockstar(_dirB+_file,"pos")

x = pos_arr[:,0]
y = pos_arr[:,1]
z = pos_arr[:,2]

xb = pos_arrB[:,0]
yb = pos_arrB[:,1]
zb = pos_arrB[:,2]

print(pos_arr.shape)
print(pos_arrB.shape)

fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(1,1,1,projection = '3d')

ax.scatter(x,y,z,s=0.2)
ax.scatter(xb,yb,zb,s=0.2)
ax.set_xlabel("$X$", size = 15)
ax.set_ylabel("$Y$", size = 15)
ax.set_zlabel("$Z$", size = 15)
plt.title("$Data B\,\,(unit:\,Mpc\,h^{-1})$", size =15)



plt.show()
