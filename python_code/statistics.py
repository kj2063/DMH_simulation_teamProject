from pygadgetreader import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from scipy import stats

# read rockstar output
_dir_A = "/media/cusped01/sjkim/CW/advastro/project/rockstar/dataA_result/"
_dir_B = "/media/cusped01/sjkim/CW/advastro/project/rockstar/dataB_result/"
_file = "halos_0"

def p(number, want):
	if number == '2' :
		return readrockstar(_dir_A + _file,  want)
	elif number =='3' :
		return readrockstar(_dir_B + _file,  want)

# --------------------------------------------------
# 1. spin parameter lambda 
spin2 = p('2','bullock_spin')
spin3 = p('3', 'bullock_spin')
mass2 = p('2', 'm')
mass3 = p('3', 'm')

mm = 10.0
spin2 = spin2[np.log10(mass2) > mm] 
spin3 = spin3[np.log10(mass3) > mm] 

print(np.nanmean(spin2), np.median(spin2))
print(np.nanmean(spin3), np.median(spin3))
print(np.nanstd(np.log(spin2)), np.nanstd(np.log(spin3)))

plt.hist(spin2, bins = 20, ls = (0, (5,3)), histtype = 'step', label = 'z = 2', density = True)
plt.hist(spin3, bins = 20, histtype = 'step', label = 'z = 3', density = True)
plt.xlim(0,0.3)
plt.xlabel("$\lambda$$^{\prime}$", size = 15)
plt.ylabel("P($\lambda$$^{\prime}$)", size = 15)
plt.legend()
plt.tick_params(axis = 'x', labelsize = 12)
plt.tick_params(axis = 'y', labelsize = 12)
plt.show()


# --------------------------------------------------
# 2. concentration c as a function of mass

rs = p('2','rs')
r = p('2', 'r')
m = p('2', 'm')

plt.hist(np.log10(m))
plt.show()

c = r/rs

#c[np.log10(m)<10.5] = np.nan
#m[np.log10(m)<10.5] = np.nan
#spin[np.log10(m)<10.5] = np.nan

ybin, edges, _ = stats.binned_statistic(np.log10(m), np.log10(c), 'median', bins = 13)
xbin = edges[:-1]
y_16, edges, _ = stats.binned_statistic(np.log10(m), np.log10(c), statistic = lambda y : np.percentile(y ,16), bins= 13) 
y_84, edges, _ = stats.binned_statistic(np.log10(m), np.log10(c), statistic = lambda y : np.percentile(y ,84), bins= 13) 

plt.plot(np.log10(m), np.log10(c), '.', color = 'orange')
plt.plot(xbin, ybin, '-.', color = 'black', linewidth = 2)
plt.plot(xbin, y_16, '--', color = 'black')
plt.plot(xbin, y_84, '--', color = 'black')
plt.xlabel("log M$_{vir}$ [h$^{-1}$ M$_{\odot}$]", size = 13)
plt.ylabel("log c", size = 15)
plt.xlim(10.0, 12)
plt.ylim(0, 2.0)
plt.show()

# 3. spin parameter and mass relation
spin2 = p('2', 'bullock_spin')
m = p('2', 'm')

ybin, edges, _ = stats.binned_statistic(np.log10(m), np.log10(spin2), 'median', bins = 10)              
xbin = edges[:-1]
y_16, edges, _ = stats.binned_statistic(np.log10(m), np.log10(spin2), statistic = lambda y : np.percentile(y ,16), bins= 10) 
y_84, edges, _ = stats.binned_statistic(np.log10(m), np.log10(spin2), statistic = lambda y : np.percentile(y ,84), bins= 10) 

plt.plot(np.log10(m), np.log10(spin2), '.', color = 'orange')
plt.plot(xbin, ybin, '-.', color = 'black', linewidth = 2)
plt.plot(xbin, y_16, '--', color = 'black')
plt.plot(xbin, y_84, '--', color = 'black')
plt.xlabel("log M$_{vir}$ [h$^{-1}$ M$_{\odot}$]", size = 13)
plt.ylabel("log $\lambda$$^{\prime}$", size = 15)
plt.xlim(10, 12)
plt.ylim(-3, 0)
plt.show()
