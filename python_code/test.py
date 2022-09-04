from pygadgetreader import *
from matplotlib import pyplot as plt
import numpy as np
#gas, dm, disk, bulge, star, bndry
#pos, vel, pid, mass, u, rho, ne, nh, hsml, sfr, age, z, pot
_dir = "/home/jun/다운로드/dataA/"
_file = "snap_best_guess_25_208_2lpt_015."
NN = range(16)[1:] #1번 파일부터 15번 파일까지 사용

data = ['pos', 'vel']
_type = ['dm', 'gas', 'star']

fig, ax = plt.subplots(2,3, figsize = (30, 10))
fig.subplots_adjust(left=0.07, bottom=0.08, right=0.99, top= 0.93, wspace=0.4, hspace=0.3)

res_xpos00 = np.array([])
res_ypos00 = np.array([])
res_xpos01 = np.array([])
res_ypos01 = np.array([])
res_xpos02 = np.array([])
res_ypos02 = np.array([])
res_xpos10 = np.array([])
res_ypos10 = np.array([])
res_xpos11 = np.array([])
res_ypos11 = np.array([])
res_xpos12 = np.array([])
res_ypos12 = np.array([])

for N in NN:
    for i in range(len(data)):
        for j in range(len(_type)):
            globals()["snap%d%d" %(i,j)] = readsnap(_dir+_file+str(N), data[i], _type[j])
            globals()["xpos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,0]
            globals()["ypos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,1]
            globals()["zpos%d%d" %(i,j)] = globals()["snap%d%d" %(i,j)][:,2]

    res_xpos00 = np.append(res_xpos00, xpos00)
    res_ypos00 = np.append(res_ypos00, ypos00)
    res_xpos01 = np.append(res_xpos01, xpos01)
    res_ypos01 = np.append(res_ypos01, ypos01)
    res_xpos02 = np.append(res_xpos02, xpos02)
    res_ypos02 = np.append(res_ypos02, ypos02)
    res_xpos10 = np.append(res_xpos10, xpos10)
    res_ypos10 = np.append(res_ypos10, ypos10)
    res_xpos11 = np.append(res_xpos11, xpos11)
    res_ypos11 = np.append(res_ypos11, ypos11)
    res_xpos12 = np.append(res_xpos12, xpos12)
    res_ypos12 = np.append(res_ypos12, ypos12)

a0 = ax[0,0].hist2d(res_xpos00, res_ypos00, bins = 1000, vmin = 0, vmax = 1200)#, cmap = 'Blues')
a1 = ax[0,1].hist2d(res_xpos01, res_ypos01, bins = 1000, vmin = 0, vmax = 1200)
a2 = ax[0,2].hist2d(res_xpos02, res_ypos02, bins = 1000, vmin = 0, vmax = 1200)
a3 = ax[1,0].hist2d(res_xpos10, res_ypos10, bins = 1000)#,vmin = 0, vmax = 100)
a4 = ax[1,1].hist2d(res_xpos11, res_ypos11, bins = 1000)#,vmin = 0, vmax = 100)
a5 = ax[1,2].hist2d(res_xpos12, res_ypos12, bins = 1000)#,vmin = 0, vmax = 100)

ax[0,0].set_title("DM Pos.", size = 20)
ax[0,0].set_xlabel("X Position", size = 15)
ax[0,0].set_ylabel("Y Position", size = 15)
ax[0,1].set_title("GAS Pos.", size = 20)
ax[0,2].set_title("STAR Pos.", size = 20)
ax[1,0].set_title("DM Vel.", size = 20)
ax[1,0].set_xlabel("X Velocity", size = 15)
ax[1,0].set_ylabel("Y Velocity", size = 15)
ax[1,1].set_title("GAS Vel.", size = 20)
ax[1,2].set_title("STAR Vel.", size = 20)

fig.colorbar(a0[3], ax = ax[0,0])
fig.colorbar(a1[3], ax = ax[0,1])
fig.colorbar(a2[3], ax = ax[0,2])
fig.colorbar(a3[3], ax = ax[1,0])
fig.colorbar(a4[3], ax = ax[1,1])
fig.colorbar(a5[3], ax = ax[1,2])

plt.tight_layout()
plt.show()

