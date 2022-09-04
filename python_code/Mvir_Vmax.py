from pygadgetreader import readrockstar
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, curve_fit
from scipy import stats

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"


m_vir = readrockstar(_dir+_file,'m')
vmax = readrockstar(_dir+_file,'vmax')

#make host halo array
a = open(_dir+"box25_parent.log", "r")
a_line = a.readlines()[16:]
a_arr = []

for l in a_line:
    if l.split(" ")[-1] == "-1\n":
        a_arr.append(l)


#make Host Halos arr about mass and Vmax        
parentA_m = np.zeros(len(a_arr))
parentA_vmax = np.zeros(len(a_arr))

for i,ii in enumerate(a_arr):
    parentA_m[i] = float(ii.split(" ")[2])
    parentA_vmax[i] = float(ii.split(" ")[3])


#non-linear fitting at Host Halos    
def f(x,a,b):
    return a*(x**(b))

pars, cov = curve_fit(f=f, xdata=parentA_m, ydata=parentA_vmax, p0 = [0,0])


x0 = np.linspace(1e9,1e13)

fig, ax = plt.subplots(1)
ax.plot(m_vir,vmax,".",label = "Sub Halo")
ax.plot(parentA_m,parentA_vmax,".", label = "Host Halo")
ax.plot(x0, pars[0]*(x0**(pars[1])), color='r', label = "Host Halo Fit")
plt.xscale('log')
plt.yscale('log')
ax.set_ylim(30,1000)
ax.set_xlim(1e9,1e13)
ax.set_ylabel("$V_{max} [km\,s^{-1}]$")
ax.set_xlabel("Halo Mass $[M_{\odot}\,h^{-1}]$")
ax.set_title("Data A (z=2)")
plt.legend()

plt.show()

