from pygadgetreader import *
from matplotlib import pyplot as plt
import numpy as np
#gas, dm, disk, bulge, star, bndry
#pos, vel, pid, mass, u, rho, ne, nh, hsml, sfr, age, z, pot
_dir = "/home/jun/work_place/astrophysics project/rockstar-master/dataA/"
_file = "snap_best_guess_25_208_2lpt_015."
NN = list(range(16))[5:]

res_xpos_dm = np.array([])
res_ypos_dm = np.array([])

for N in NN:
    a = readsnap(_dir+_file+str(N), 'pos','dm')
    
    res_xpos_dm = np.append(res_xpos_dm, a[:,0])
    res_ypos_dm = np.append(res_ypos_dm, a[:,1])

fig, ax = plt.subplots(1)
ax.hist2d(res_xpos_dm, res_ypos_dm, bins = 1000, vmin = 10, vmax = 1000 )

plt.show()
