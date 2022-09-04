from pygadgetreader import *
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#gas, dm, disk, bulge, star, bndry
#pos, vel, pid, mass, u, rho, ne, nh, hsml, sfr, age, z, pot
_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA/"
_file = "snap_best_guess_25_208_2lpt_015"
NN = 1
data = ['pos', 'vel']
_type = ['dm', 'gas', 'star']
for i in range(len(data)):
    for j in range(len(_type)):
        globals()["snap%d%d" %(i,j)] = readsnap(_dir+_file , data[i], _type[j])
        globals()["xpos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,0]
        globals()["ypos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,1]
        globals()["zpos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,2]

fig, ax = plt.subplots(2,3, figsize = (30, 10))
fig.subplots_adjust(left=0.07, bottom=0.08, right=0.99, top= 0.93, wspace=0.4, hspace=0.3)
a0 = ax[0,0].hist2d(xpos00, ypos00, bins = 1000, vmin =0, vmax = 90)#, cmap = 'Blues')
ax[0,0].set_title("DM Pos.", size = 20)
ax[0,0].set_xlabel("X Position", size = 15)
ax[0,0].set_ylabel("Y Position", size = 15)
a1 = ax[0,1].hist2d(xpos01, ypos01, bins = 1000, vmin =0, vmax = 70)
ax[0,1].set_title("GAS Pos.", size = 20)
a2 = ax[0,2].hist2d(xpos02, ypos02, bins = 1000, vmin = 0, vmax = 100)
ax[0,2].set_title("STAR Pos.", size = 20)
a3 = ax[1,0].hist2d(xpos10, ypos10, bins = 1000)#, vmin = 0, vmax = 100)
ax[1,0].set_title("DM Vel.", size = 20)
ax[1,0].set_xlabel("X Velocity", size = 15)
ax[1,0].set_ylabel("Y Velocity", size = 15)
a4 = ax[1,1].hist2d(xpos11, ypos11, bins = 1000)#, vmin = 0, vmax = 100)
ax[1,1].set_title("GAS Vel.", size = 20)
a5 = ax[1,2].hist2d(xpos12, ypos12, bins = 1000)#, vmin = 0, vmax = 100)
ax[1,2].set_title("STAR Vel.", size = 20)
fig.colorbar(a0[3], ax = ax[0,0])
fig.colorbar(a1[3], ax = ax[0,1])
fig.colorbar(a2[3], ax = ax[0,2])
fig.colorbar(a3[3], ax = ax[1,0])
fig.colorbar(a4[3], ax = ax[1,1])
fig.colorbar(a5[3], ax = ax[1,2])
plt.show()

fig = plt.figure(figsize = (13,13))
ax = fig.add_subplot(1,1,1,projection = '3d')
ax.scatter(xpos00,ypos00,zpos00,s=0.1)
plt.show()
