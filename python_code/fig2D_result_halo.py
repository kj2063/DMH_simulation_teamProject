from pygadgetreader import readrockstar
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"

pos_arr = readrockstar(_dir+_file,"pos")

x = pos_arr[:,0]
y = pos_arr[:,1]

fig ,ax =plt.subplots(1)

ax.plot(x,y,',')
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.title("DM Halos Pos (unit: Mpc/h)")



plt.show()
