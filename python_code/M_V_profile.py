from pygadgetreader import readrockstar
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, curve_fit
from scipy import stats

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"

#r_vir = readrockstar(_dir+_file,"r")
#r_s = readrockstar(_dir+_file,"rs")

m_vir = readrockstar(_dir+_file,"m")

#corvel_arr = readrockstar(_dir+_file,'corevel')
#bulkvel_arr = readrockstar(_dir+_file,'bulkvel')

vmax = readrockstar(_dir+_file,'vmax')

#cor_vel = np.sqrt(corvel_arr[:,0]**2 + corvel_arr[:,1]**2 + corvel_arr[:,2]**2)
#bulk_vel = np.sqrt(bulkvel_arr[:,0]**2 + bulkvel_arr[:,1]**2 + bulkvel_arr[:,2]**2)

a = open(_dir+"box25_parent.log", "r")
a_line = a.readlines()[16:]
a_arr = []

for l in a_line:
    if l.split(" ")[-1] == "-1\n":
        a_arr.append(l)

parentA_m = np.zeros(len(a_arr))
parentA_vmax = np.zeros(len(a_arr))


for i,ii in enumerate(a_arr):
    parentA_m[i] = float(ii.split(" ")[2])
    parentA_vmax[i] = float(ii.split(" ")[3])

#vel = readrockstar(_dir+_file,"vrms")
#x = np.linspace(1,20)
#y = np.sqrt(1/x)
#c_to_a = readrockstar(_dir+_file,'c_to_a')
#b_to_a = readrockstar(_dir+_file,'b_to_a')
Voff = readrockstar(_dir+_file,'Voff')

#def f(x):
#    return np.log(1+x) + x/(1+x)

#def density(r):
#    return (f(r/r_s)*m_vir)/(4*np.pi*f(r_vir/r_s)*((r_s)**3)*(r/r_s)*((1+r/r_s)**2))
def f(x,a,b):
    return a*(x**(b))


pars, cov = curve_fit(f=f, xdata=parentA_m, ydata=parentA_vmax, p0 = [0,0])

print(pars)



x0 = np.linspace(1e9,1e13)


fig, ax = plt.subplots(1)
ax.plot(m_vir,vmax,".",label = "Sub Halo")
ax.plot(parentA_m,parentA_vmax,".", label = "Host Halo")
#ax.plot(x0,exponential(x0,0.05,1e-13,10)) 
#ybin, edges, _ = stats.binned_statistic(parentA_m, parentA_vmax, 'mean', bins = 10)
#xbin = edges[:-1]
#plt.plot(xbin, ybin, '-.', markersize = 10)
ax.plot(x0, pars[0]*(x0**(pars[1])),color='r', label = "Host Halo Fit")
#ax.plot(x0, res.x[0]*x0+res.x[1], color = 'r')
plt.xscale('log')
plt.yscale('log')
ax.set_ylim(30,1000)
ax.set_xlim(1e9,1e13)
ax.set_ylabel("$V_{max} [km\,s^{-1}]$")
ax.set_xlabel("Halo Mass $[M_{\odot}\,h^{-1}]$")
ax.set_title("Data A (z=2)")
plt.legend()

plt.show()

