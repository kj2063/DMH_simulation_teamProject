# Shin-Jeong Kim 
# Department of Astronomy and Space Science
# 2021.06.12
# correlation plot between halo properties obtained from Rockstar 


import seaborn as sns
from pygadgetreader import *                                                    
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from scipy import stats
import pandas as pd

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
# corrrelation between spin parameter, c, Xoff, T

spin = p('2','bullock_spin')
mass = p('2', 'm')
r = p('2', 'r')
rs = p('2', 'rs')
c = r/rs

Xoff = p('2', 'Xoff')
b_to_a = np.array(p('2', 'b_to_a'))
c_to_a = np.array(p('2', 'c_to_a'))
T = (1-(b_to_a)**2)/(1-(c_to_a)**2)
#T = c_to_a

# mass cut #
mm = 10.5
spin = spin[np.log10(mass) > mm]
c = c[np.log10(mass) > mm]
Xoff = Xoff[np.log10(mass) > mm]
T = T[np.log10(mass) > mm]
b_to_a = b_to_a[np.log10(mass) > mm]
c_to_a = c_to_a[np.log10(mass) > mm]
mass = mass[np.log10(mass) > mm]

print(len(spin), len(Xoff))
d = {"log Mvir" : np.log10(mass), "log ${\lambda}\prime$" : np.log10(spin), "log c" : np.log10(c), "log Xoff" : np.log10(Xoff), "b/a" : b_to_a, "c/a" : c_to_a}

df = pd.DataFrame(data = d)
def corrfunc(x,y, **kws):
	r, p = stats.pearsonr(x,y)
	p_stars = ''
	if p <= 0.05 :
		p_stars = '*'
	if p <= 0.01 :
		p_stars = '**'
	if p <= 0.001:
		p_stars = '***'

	if abs(r) > 0.25 :
		ax = plt.gca()
		ax.annotate('{:.2f}'.format(r) + p_stars, xy=(0.05, 0.9), xycoords=ax.transAxes, fontsize = 15, color ='red')
	elif abs(r) < 0.25 :
		ax = plt.gca()
		ax.annotate('{:.2f}'.format(r) + p_stars, xy=(0.05, 0.9), xycoords=ax.transAxes, fontsize = 15, color ='black')


fig, ax = plt.subplots(figsize = (20,20))
fig.subplots_adjust(left=0.1, bottom=0.10, right=0.95, top= 0.95, wspace=0.0, hspace=0.2)

mask = np.zeros_like(df.corr(), dtype = np.bool)
mask[np.triu_indices_from(mask)] = True
g1 = sns.PairGrid(df, size = 2 , corner = True, height = 3)
g1.map_diag(sns.distplot, kde = False)
g1.map_lower(corrfunc )
g1.map_lower(sns.kdeplot, cmap = "Blues_d" )
g1.fig.subplots_adjust(wspace = .02, hspace = .02)
plt.rcParams["axes.labelsize"] = 15
plt.show()


