from pygadgetreader import *
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import sys
from matplotlib.colors import LogNorm

#gas, dm, disk, bulge, star, bndry
#pos, vel, pid, mass, u, rho, ne, nh, hsml, sfr, age, z, pot

def colorbar(mappable):
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax)
    plt.sca(last_axes)
    return cbar

_dir_A = "/media/cusped01/sjkim/CW/advastro/project/data_projects_1_2_advanced_astrophysics_spring_2021_A/best_guess_25_208/snapdir_015/snap_best_guess_25_208_2lpt_015"
_dir_B = "/media/cusped01/sjkim/CW/advastro/project/data_projects_1_2_advanced_astrophysics_spring_2021_B/best_guess_25_208/snapdir_010/snap_best_guess_25_208_2lpt_010"

data = [_dir_B, _dir_A]
_type = ['dm', 'gas', 'star']

#--------------simulation information -----#
i = 0
print(readheader(data[i], 'time'))
print(readheader(data[i], 'redshift'))
print(readheader(data[i], 'boxsize'))
print(readheader(data[i], 'O0'))
print(readheader(data[i], 'Ol'))
print(readheader(data[i], 'h'))
print(readheader(data[i], 'gascount'))
print(readheader(data[i], 'dmcount'))
print(readheader(data[i], 'starcount'))
print(readheader(data[i], 'f_sfr'))
print(readheader(data[i], 'f_fb'))
print(readheader(data[i], 'f_cooling'))
print(readheader(data[i], 'f_age'))
print(readheader(data[i], 'f_metals'))
print(readheader(data[i], 'npartTotal'))
#print(readheader(data[i], 'header'))


for i in range(len(data)):
	for j in range(len(_type)):
		globals()["snap%d%d" %(i,j)] = readsnap(data[i], 'pos', _type[j])
		globals()["xpos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,0]/1000
		globals()["ypos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,1]/1000
		globals()["zpos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,2]/1000

		#indices = np.arange(0, len(globals()["xpos%d%d" %(i,j)]), 300)
		#globals()["xpos%d%d" %(i,j)] = globals()["xpos%d%d" %(i,j)][indices]
		#globals()["ypos%d%d" %(i,j)] = globals()["ypos%d%d" %(i,j)][indices]
		#globals()["zpos%d%d" %(i,j)] = globals()["zpos%d%d" %(i,j)][indices]

#idx = np.arange(0,len(xpos00), 2)
#fig = plt.figure(figsize = (13,13))
#ax = fig.add_subplot(1,1,1, projection = '3d')
#ax.scatter(xpos00[idx], ypos00[idx], zpos00[idx], s = 1)
#plt.show()

fig, ax = plt.subplots(2,3, figsize = (30, 10))
fig.subplots_adjust(left=0.07, bottom=0.08, right=0.99, top= 0.93, wspace=0.2, hspace=0.3)                                                                     
a0 = ax[0,0].hist2d(xpos00, ypos00, bins = 1000, vmin = 0, vmax = 70, label = 'z = 3', cmap = 'Greys')
ax[0,0].set_title("z = 3, DM", size = 20)
ax[0,0].set_xlabel("X[h$^{-1}$Mpc]", size = 15)
ax[0,0].set_ylabel("Y[h$^{-1}$Mpc]", size = 15)
a1 = ax[0,1].hist2d(xpos01, ypos01, bins = 1000, vmin = 0, vmax = 70, cmap = 'Greys')
ax[0,1].set_xlabel("X[h$^{-1}$Mpc]", size = 15)
ax[0,1].set_ylabel("Y[h$^{-1}$Mpc]", size = 15)
ax[0,1].set_title("Gas", size = 20)
a2 = ax[0,2].hist2d(xpos02, ypos02, bins = 800, vmin = 0, vmax = 35, cmap = 'Greys')
ax[0,2].set_xlabel("X[h$^{-1}$Mpc]", size = 15)
ax[0,2].set_ylabel("Y[h$^{-1}$Mpc]", size = 15)
ax[0,2].set_title("Star", size = 20)

a3 = ax[1,0].hist2d(xpos10, ypos10, bins = 1000, vmin = 0, vmax = 70, label = 'z = 2', cmap = 'Greys')
ax[1,0].set_title("z = 2, DM", size = 20)
ax[1,0].set_xlabel("X[h$^{-1}$Mpc]", size = 15)
ax[1,0].set_ylabel("Y[h$^{-1}$Mpc]", size = 15)
a4 = ax[1,1].hist2d(xpos11, ypos11, bins = 1000, vmin = 0, vmax = 70, cmap = 'Greys')
ax[1,1].set_title("Gas", size = 20)
ax[1,1].set_xlabel("X[h$^{-1}$Mpc]", size = 15)
ax[1,1].set_ylabel("Y[h$^{-1}$Mpc]", size = 15)
a5 = ax[1,2].hist2d(xpos12, ypos12, bins = 800, vmin = 0, vmax = 35, cmap = 'Greys')
ax[1,2].set_xlabel("X[h$^{-1}$Mpc]", size = 15)
ax[1,2].set_ylabel("Y[h$^{-1}$Mpc]", size = 15)
ax[1,2].set_title("Star", size = 20)

colorbar(a0[3])
colorbar(a1[3])
colorbar(a2[3])
colorbar(a3[3])
colorbar(a4[3])
colorbar(a5[3])
#fig.colorbar(a0[3], ax = ax[0,0])
#fig.colorbar(a1[3], ax = ax[0,1])
#fig.colorbar(a2[3], ax = ax[0,2])
#fig.colorbar(a3[3], ax = ax[1,0])
#fig.colorbar(a4[3], ax = ax[1,1])
#fig.colorbar(a5[3], ax = ax[1,2])
#plt.show()


