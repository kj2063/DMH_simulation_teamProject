from pygadgetreader import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import sys

# read rockstar output
_dir_A = "/media/cusped01/sjkim/CW/advastro/project/rockstar/dataA_result/"
_dir_B = "/media/cusped01/sjkim/CW/advastro/project/rockstar/dataB_result/"
_dir = [_dir_A, _dir_B]
_file = "halos_0"

for i in range(2):
	dir_ = _dir[i]
	globals()['pos%s' %(i+2)] = readrockstar(dir_ + _file, "pos")
	globals()['xpos%s' %(i+2)], globals()['ypos%s' %(i+2)], globals()['zpos%s' %(i+2)] = globals()['pos%s' %(i+2)][:,0], globals()['pos%s' %(i+2)][:,1], globals()['pos%s' %(i+2)][:,2] # Mpc/h unit
	globals()['mass%s' %(i+2)] = readrockstar(dir_ + _file, 'm')
	globals()['radius%s' %(i+2)] = readrockstar(dir_ + _file, 'r')

#	globals()["xpos%s" %(i+2)] *= 1000
#	globals()["ypos%s" %(i+2)] *= 1000
#	globals()["zpos%s" %(i+2)] *= 1000 # Mpc/h => kpc/h unit conversion

	globals()["xpos%s" %(i+2)][np.log10(globals()["mass%s" %(i+2)])<11] = np.nan
	globals()["ypos%s" %(i+2)][np.log10(globals()["mass%s" %(i+2)])<11] = np.nan
	globals()["radius%s" %(i+2)][np.log10(globals()["mass%s" %(i+2)])<11] = np.nan

#fig = plt.figure(figsize = (13,13))
#ax = fig.add_subplot(1,1,1, projection = '3d')
#ax.scatter(xpos, ypos, zpos, s = 0.1)
#plt.show()

# overplot on the snapshot
snap_fileA = "/media/cusped01/sjkim/CW/advastro/project/data_projects_1_2_advanced_astrophysics_spring_2021_A/best_guess_25_208/snapdir_015/snap_best_guess_25_208_2lpt_015" 
data_posA = readsnap(snap_fileA, "pos", 'dm')/1000 # kpc/h => Mpc/h unit conversiont
data_xposA, data_yposA, data_zposA = data_posA[:,0], data_posA[:,1], data_posA[:,2]

snap_fileB = "/media/cusped01/sjkim/CW/advastro/project/data_projects_1_2_advanced_astrophysics_spring_2021_B/best_guess_25_208/snapdir_010/snap_best_guess_25_208_2lpt_010"
data_posB = readsnap(snap_fileB, "pos", 'dm')/1000 # kpc/h => Mpc/h unit conversion
data_xposB, data_yposB, data_zposB = data_posB[:,0], data_posB[:,1], data_posB[:,2]

fig,ax = plt.subplots(1,2, sharex = True, sharey = True,figsize = (20,10))#, sharey= True)                                                
ax[0].hist2d(data_xposA, data_yposA, bins = 1000, norm = LogNorm())
ax[0].scatter(xpos2,ypos2, color = 'white', s = radius2, facecolors = 'none')
ax[0].set_xlabel("X [h$^{-1}$ Mpc]", size = 15)
ax[0].set_ylabel("Y [h$^{-1}$ Mpc]", size = 15)
ax[0].set_title("z = 2", size = 20)
ax[1].hist2d(data_xposB, data_yposB, bins = 1000, norm = LogNorm())
ax[1].scatter(xpos3,ypos3, color = 'white', s = radius3, facecolors = 'none')
ax[1].set_xlabel("X [h$^{-1}$ Mpc]", size = 15)
ax[1].set_ylabel("Y [h$^{-1}$ Mpc]", size = 15)
ax[1].set_title("z = 3", size = 20)
plt.show()

# plot the halo mass function 
plt.hist(np.log10(mass2), bins = 20, histtype = 'step', label = 'z = 2', density = True)
plt.hist(np.log10(mass3), bins = 20, histtype = 'step', label = 'z = 3', density = True)
plt.xlabel("log(Halo Mass) [M$_{\odot}$/h]", size = 15)
plt.ylabel("N", size = 15)
plt.legend()
plt.show()
