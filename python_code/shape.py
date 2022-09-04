from pygadgetreader import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


# read rockstar output
_dir_A = "/media/cusped01/sjkim/CW/advastro/project/rockstar/dataA_result/"
_dir_B = "/media/cusped01/sjkim/CW/advastro/project/rockstar/dataB_result/"
_dir = [_dir_A, _dir_B]
zz = [2,3]

_file = "halos_0"

for i in range(len(_dir)):
	dir__ = _dir[i]
	
	mm = 10.0
	# 10.0 < log10(Mvir) 
	globals()["b_to_a%s" %(zz[i])] = readrockstar(dir__ + _file, "b_to_a")
	globals()["c_to_a%s" %(zz[i])] = readrockstar(dir__ + _file, "c_to_a")
	globals()["mass%s" %(zz[i])] = readrockstar(dir__ + _file, 'm')

	globals()["b_to_a%s" %(zz[i])] = globals()["b_to_a%s" %(zz[i])][np.log10(globals()["mass%s" %(zz[i])]) > mm ] 
	globals()["c_to_a%s" %(zz[i])] = globals()["c_to_a%s" %(zz[i])][np.log10(globals()["mass%s" %(zz[i])]) > mm ] 
	globals()["mass%s" %(zz[i])] = globals()["mass%s" %(zz[i])][np.log10(globals()["mass%s" %(zz[i])]) > mm ] 


# plot T value 1/3, 2/3
xx = np.linspace(0,1, 100)
TT1_3 = np.sqrt(1/3.*xx**2 + 2/3.)
TT2_3 = np.sqrt(2/3.*xx**2 + 1/3.)


# plot the c/a vs b/a 
fig,ax = plt.subplots(1,2, sharex = True, sharey= True)
fig.subplots_adjust(left=0.1, bottom=0.10, right=0.95, top= 0.95, wspace=0.2, hspace=0.2)

ax[0].plot(c_to_a2, b_to_a2, '.', color = 'darkblue', markersize = 1.5)
ax[0].plot(xx, TT1_3, color = 'black', linewidth = 0.5)
ax[0].plot(xx, TT2_3, color = 'black', linewidth = 0.5)
ax[0].set_xlabel("c/a", size = 20)
ax[0].set_ylabel("b/a", size = 20)
ax[0].set_title("z = 2", size = 15)
ax[0].text(0.01, 0.9, "Oblate")
ax[0].text(0.01, 0.7, "Triaxial")
ax[0].text(0.01, 0.5, "Prolate")
ax[0].tick_params(axis = 'x', labelsize = 15)
ax[0].tick_params(axis = 'y', labelsize = 15)
ax[1].plot(c_to_a3, b_to_a3, '.', color = 'darkblue', markersize = 1.5)
ax[1].plot(xx, TT1_3, color = 'black', linewidth = 0.5)
ax[1].plot(xx, TT2_3, color = 'black', linewidth = 0.5)
ax[1].set_xlabel("c/a", size = 20)
ax[1].set_title("z = 3", size = 15)
ax[1].text(0.01, 0.9, "Oblate")
ax[1].text(0.01, 0.7, "Triaxial")
ax[1].text(0.01, 0.5, "Prolate")
ax[1].tick_params(axis = 'x', labelsize = 15)
ax[1].tick_params(axis = 'y', labelsize = 15)
fig.tight_layout()
plt.show()

#------------------------------T histogram --------------------------------
mm2 = 11
mass_1 = mass2[np.log10(mass2) < mm2]
b_to_a_1 = b_to_a2[np.log10(mass2) < mm2]
c_to_a_1 = c_to_a2[np.log10(mass2) < mm2]

mm3 = 12
mass_2 = mass2[(np.log10(mass2) > mm2) & (np.log10(mass2) < mm3)]
b_to_a_2 = b_to_a2[(np.log10(mass2) > mm2) & (np.log10(mass2) < mm3)]
c_to_a_2 = c_to_a2[(np.log10(mass2) > mm2) & (np.log10(mass2) < mm3)]

mass_3 = mass2[np.log10(mass2) > mm3]
b_to_a_3 = b_to_a2[np.log10(mass2) > mm3]
c_to_a_3 = c_to_a2[np.log10(mass2) > mm3]

# redshift 3
mass_1b = mass3[np.log10(mass3) < mm2]
b_to_a_1b = b_to_a3[np.log10(mass3) < mm2]
c_to_a_1b = c_to_a3[np.log10(mass3) < mm2]

mass_2b = mass3[(np.log10(mass3) > mm2) & (np.log10(mass3) < mm3)]
b_to_a_2b = b_to_a3[(np.log10(mass3) > mm2) & (np.log10(mass3) < mm3)]
c_to_a_2b = c_to_a3[(np.log10(mass3) > mm2) & (np.log10(mass3) < mm3)]

mass_3b = mass3[np.log10(mass3) > mm3]
b_to_a_3b = b_to_a3[np.log10(mass3) > mm3]
c_to_a_3b = c_to_a3[np.log10(mass3) > mm3]

#plt.hist(np.log10(mass_1), histtype = 'step')
#plt.hist(np.log10(mass_2), histtype = 'step')
#plt.hist(np.log10(mass_3), histtype = 'step')
#plt.show()
#
#plt.hist(np.log10(mass_1b), histtype = 'step')
#plt.hist(np.log10(mass_2b), histtype = 'step')
#plt.hist(np.log10(mass_3b), histtype = 'step')
#plt.show()


# calcuate T indicating the halo shape
# redshit 2
T_1 = (1-np.array(b_to_a_1)**2)/(1-np.array(c_to_a_1)**2)
T_2 = (1-np.array(b_to_a_2)**2)/(1-np.array(c_to_a_2)**2)
T_3 = (1-np.array(b_to_a_3)**2)/(1-np.array(c_to_a_3)**2)

# redshit 3
T_1b = (1-np.array(b_to_a_1b)**2)/(1-np.array(c_to_a_1b)**2)
T_2b = (1-np.array(b_to_a_2b)**2)/(1-np.array(c_to_a_2b)**2)
T_3b = (1-np.array(b_to_a_3b)**2)/(1-np.array(c_to_a_3b)**2)

print("%.2f, %.2f" %( (T_1 < 1/3.).sum()/len(T_1), (T_1 > 2/3.).sum()/len(T_1)))
print("%.2f, %.2f" %( (T_2 < 1/3.).sum()/len(T_2), (T_2 > 2/3.).sum()/len(T_2)))
print("%.2f, %.2f" %( (T_3 < 1/3.).sum()/len(T_3), (T_3 > 2/3.).sum()/len(T_3)))

print("%.2f, %.2f" %( (T_1b < 1/3.).sum()/len(T_1b), (T_1b > 2/3.).sum()/len(T_1b)))
print("%.2f, %.2f" %( (T_2b < 1/3.).sum()/len(T_2b), (T_2b > 2/3.).sum()/len(T_2b)))
print("%.2f, %.2f" %( (T_3b < 1/3.).sum()/len(T_3b), (T_3b > 2/3.).sum()/len(T_3b)))


fig,ax = plt.subplots(1,3, sharex = True, sharey= True)
fig.subplots_adjust(left=0.1, bottom=0.15, right=0.95, top= 0.90, wspace=0.0, hspace=0.2)

ax[0].hist(T_1, density = True, color = 'white', ls = (0,(5,5)), edgecolor = 'black', histtype = 'step', label = 'z = 2')
ax[0].hist(T_1b, density = True, color = 'white', edgecolor = 'black', histtype = 'step', label = 'z = 3')
ax[0].axvline(x = 0.333, ls = '--', color = 'grey')
ax[0].axvline(x = 0.666, ls = '--', color = 'grey')
ax[0].set_ylabel("P(T)", size = 20)
ax[0].text(0.20, 5.1, "O", size = 20)
ax[0].text(0.5, 5.1, "T", size = 20)
ax[0].text(0.80,5.1, "P", size = 20)
ax[0].tick_params(axis = 'x', labelsize = 15)
ax[0].tick_params(axis = 'y', labelsize = 15)
ax[0].legend()
ax[0].set_ylim(0,5.0)
ax[1].hist(T_2, density = True, color = 'white', ls = (0,(5,5)), edgecolor = 'darkorange', histtype = 'step', label = 'z = 2')
ax[1].hist(T_2b, density = True, color = 'white', edgecolor = 'darkorange', histtype = 'step', label = 'z = 3')
ax[1].axvline(x = 0.333, ls = '--', color = 'grey')
ax[1].axvline(x = 0.666, ls = '--', color = 'grey')
ax[1].set_xlabel("T", size = 20)
ax[1].text(0.20, 5.1, "O", size = 20)
ax[1].text(0.5, 5.1, "T", size = 20)
ax[1].text(0.80,5.1, "P", size = 20)
ax[1].tick_params(axis = 'x', labelsize = 15)
ax[1].tick_params(axis = 'y', labelsize = 15)
ax[1].legend()
ax[2].hist(T_3, density = True, color = 'white', ls = (0,(5,5)), edgecolor = 'darkblue', histtype = 'step', label = 'z = 2')
ax[2].hist(T_3b, density = True, color = 'white', edgecolor = 'darkblue', histtype = 'step', label = 'z = 3')
ax[2].axvline(x = 0.333, ls = '--', color = 'grey')
ax[2].axvline(x = 0.666, ls = '--', color = 'grey')
ax[2].text(0.20, 5.1, "O", size = 20)
ax[2].text(0.5, 5.1, "T", size = 20)
ax[2].text(0.80,5.1, "P", size = 20)
ax[2].tick_params(axis = 'x', labelsize = 15)
ax[2].tick_params(axis = 'y', labelsize = 15)
ax[2].legend()
'''
ax[3].hist(T_4, density = True, color = 'white', edgecolor = 'darkorange', histtype = 'step')
ax[3].axvline(x = 0.333, ls = '--', color = 'grey')
ax[3].axvline(x = 0.666, ls = '--', color = 'grey')
ax[3].set_xlabel("T", size = 15)
ax[3].set_ylabel("P(T) at z = 3", size = 15)
ax[3].text(0.20, 2.7, "O", size = 15)
ax[3].text(0.5, 2.7, "T", size = 15)
ax[3].text(0.80,2.7, "P", size = 15)
ax[3].legend()

ax[4].hist(T_5, density = True, color = 'white', edgecolor = 'darkorange', histtype = 'step')
ax[4].axvline(x = 0.333, ls = '--', color = 'grey')
ax[4].axvline(x = 0.666, ls = '--', color = 'grey')
ax[4].set_xlabel("T", size = 15)
ax[4].set_ylabel("P(T) at z = 3", size = 15)
ax[4].text(0.20, 2.7, "O", size = 15)
ax[4].text(0.5, 2.7, "T", size = 15)
ax[4].text(0.80,2.7, "P", size = 15)
ax[4].legend()
'''
plt.show()

# ------------------------------------------------------------------------------
# mean c/a as a function of halo mass
m2 = np.log10(readrockstar(_dir_A + _file, 'm'))
s2 = readrockstar(_dir_A + _file, "c_to_a")
i2 = readrockstar(_dir_A + _file, "b_to_a")
m3 = np.log10(readrockstar(_dir_B + _file, 'm'))
s3 = readrockstar(_dir_B + _file, "c_to_a")
i3 = readrockstar(_dir_B + _file, "b_to_a")

from scipy import stats

ybin2, edges2, _ = stats.binned_statistic(m2, s2, 'mean', bins = 10)
xbin2 = edges2[:-1]

ybin2i, edges2i, _ = stats.binned_statistic(m2, i2, 'mean', bins = 10)
xbin2i = edges2[:-1]

fig,ax = plt.subplots(1,2, sharex = True)#, sharey= True)
fig.subplots_adjust(left=0.15, bottom=0.15, right=0.95, top= 0.95, wspace=0.4, hspace=0.2)

ax[0].plot(xbin2, ybin2, '-.', markersize = 10, label = 'z= 2')
ax[0].set_xlabel("log M$_{vir}$ (M$_{\odot}$ h$^{-1}$)", size = 15)
ax[0].set_ylabel("<c/a>", size = 15)
ax[0].set_xlim(10.5,12.5)
ax[0].set_ylim(0.4, 0.6)
#ax[0].legend()
ax[1].plot(xbin2i, (ybin2i), '-.', markersize = 10, label = 'z= 2')
ax[1].set_xlabel("log M$_{vir}$ (M$_{\odot}$ h$^{-1}$)", size = 15)
ax[1].set_ylabel("<b/a>", size = 15)
ax[1].set_xlim(10.5,12.5)
ax[1].set_ylim(0.6, 0.8)
#ax[1].legend()
plt.show()
