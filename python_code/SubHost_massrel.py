from pygadgetreader import readrockstar
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, curve_fit
from scipy import stats
import heapq

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"

#r_vir = readrockstar(_dir+_file,"r")
#r_s = readrockstar(_dir+_file,"rs")

m_vir = readrockstar(_dir+_file,"m")
#print(len(m_vir))

#fig, ax = plt.subplots(1)
#ax.hist(np.log10(m_vir))
#ax.set_xscale('log')
#ax.set_yscale('log')
#plt.show()

#corvel_arr = readrockstar(_dir+_file,'corevel')
#bulkvel_arr = readrockstar(_dir+_file,'bulkvel')

#vmax = readrockstar(_dir+_file,'vmax')

#cor_vel = np.sqrt(corvel_arr[:,0]**2 + corvel_arr[:,1]**2 + corvel_arr[:,2]**2)
#bulk_vel = np.sqrt(bulkvel_arr[:,0]**2 + bulkvel_arr[:,1]**2 + bulkvel_arr[:,2]**2)

a = open(_dir+"box25_parent.log", "r")
a_line = a.readlines()[16:]

host_arr = []
sub_arr = []

b = open(_dir+"out_0.list", "r")
b_line = b.readlines()[16:]

print(b_line[0])

for l in a_line:
    if l.split(" ")[-1] == "-1\n":
        host_arr.append(l)

for l in a_line:
    if l.split(" ")[-1] != "-1\n":
        sub_arr.append(l)

host_sub = np.zeros(len(b_line))
count = np.zeros(len(b_line))

for ii,i in enumerate(b_line):
    for j in sub_arr:
        if int(i.split(" ")[0]) == int(j.split(" ")[-1]):
            count[ii] += 1

count = list(count)
print(count[8307],count[8152])


print(heapq.nlargest(30, xrange(len(count)), key=count.__getitem__))

#[1191, 2542, 8215, 2550, 16132, 3493, 8309, 1279, 14667, 8307, 13411, 16008, 11948, 28, 8152]



#max_list = []
#
#for i in sub_arr:
#    if int(i.split(" ")[-1]) == count.index(max(count)):
#        max_list.append(i)
#
#print(len(max_list))
#c= open('sub_halo_maxlist.txt', 'w')
#
#for i in max_list:
#    c.write(i)
#
#c.close()


###host_m = np.zeros(len(host_arr))
###host_vmax = np.zeros(len(host_arr))
###
###sub_m = np.zeros(len(sub_arr))
###
###
#
#for i,ii in enumerate(host_arr):
#    host_m[i] = float(ii.split(" ")[2])
#    host_vmax[i] = float(ii.split(" ")[3])
#
#for j,jj in enumerate(sub_arr):
#    sub_m[j] = float(jj.split(" ")[2])
#
#
#print(len(host_m))
#print(len(sub_m))
#
##vel = readrockstar(_dir+_file,"vrms")
##x = np.linspace(1,20)
##y = np.sqrt(1/x)
##c_to_a = readrockstar(_dir+_file,'c_to_a')
##b_to_a = readrockstar(_dir+_file,'b_to_a')
##Voff = readrockstar(_dir+_file,'Voff')
#
##def f(x):
##    return np.log(1+x) + x/(1+x)
#
##def density(r):
##    return (f(r/r_s)*m_vir)/(4*np.pi*f(r_vir/r_s)*((r_s)**3)*(r/r_s)*((1+r/r_s)**2))
##def f(x,a,b):
##    return a*(x**(b))
#
#
##pars, cov = curve_fit(f=f, xdata=host_m, ydata=host_vmax, p0 = [0,0])
#
##print(pars)
#
#fig, ax = plt.subplots(1)
#ax.hist(np.log10(host_m), alpha = 0.6 ,label = "host halo",bins =40 ,density = True)
#ax.hist(np.log10(sub_m), alpha = 0.6, label = "sub halo",bins = 40 ,density = True)
#ax.set_xscale('log')
#plt.legend()
#plt.show()
#
#x0 = np.linspace(1e9,1e13)
##
##fig, ax = plt.subplots(1)
##ax.plot(m_vir,vmax,".",label = "Sub Halo")
##ax.plot(host_m,host_vmax,".", label = "Host Halo")
###ax.plot(x0,exponential(x0,0.05,1e-13,10)) 
###ybin, edges, _ = stats.binned_statistic(parentA_m, parentA_vmax, 'mean', bins = 10)
###xbin = edges[:-1]
###plt.plot(xbin, ybin, '-.', markersize = 10)
##ax.plot(x0, pars[0]*(x0**(pars[1])),color='r', label = "Host Halo Fit")
###ax.plot(x0, res.x[0]*x0+res.x[1], color = 'r')
##plt.xscale('log')
##plt.yscale('log')
##ax.set_ylim(30,1000)
##ax.set_xlim(1e9,1e13)
##ax.set_ylabel("$V_{max} [km\,s^{-1}]$")
##ax.set_xlabel("Halo Mass $[M_{\odot}\,h^{-1}]$")
##ax.set_title("Data A (z=2)")
##plt.legend()
##
##plt.show()
##
