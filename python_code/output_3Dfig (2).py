from pygadgetreader import readrockstar
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"

pos_arr = readrockstar(_dir+_file,"pos")

x = pos_arr[:,0]
y = pos_arr[:,1]
z = pos_arr[:,2]

fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(1,1,1,projection = '3d')

ax.scatter(x,y,z,s=0.2)
ax.set_xlabel("$X$")
ax.set_ylabel("$Y$")
ax.set_zlabel("$Z$")
plt.title("$Data A\,\,(unit:\,Mpc\,h^{-1})$")



plt.show()
