import numpy as np
import matplotlib.pyplot as plt

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"

a = open(_dir+'box25_parent.log','r')
sub_line = a.readlines()[16:]

b = open(_dir+'out_0.list','r')
all_line = b.readlines()[16:]

fig, ax = plt.subplots(2)
#num_list = [1191,2542,8215,2550,16132,3493,8309,1279,14667,8307,13411,16008,11948,28,8152]
#num_list = [1191, 2542, 2550, 16132, 3493, 1279, 14667, 13411, 16008, 28, 14709, 2540, 4761, 17514, 16031, 45, 3580, 4787]
num_list = [1191, 2542, 2550, 16132, 3493, 1279, 14667, 13411, 16008, 28, 14709, 2540, 4761, 17514, 16031, 45, 3580, 4787, 14690, 18814, 66, 2535, 3543, 2609, 4766, 4803, 16022, 16065]

#num_list = [1191,2542,2550,16132,3493,1279,14667,13411,16008,28]

m_mean_sub = []
m_host = []
number_sub = []

Rvir_host = []
Rs_host = []


for i in num_list:
    sub_list = []
    
    for j in sub_line:
        if i == int(j.split(' ')[-1]):
            sub_list.append(float(j.split(' ')[2]))
    
    number_sub.append(len(sub_list))

    print(number_sub)
    m_h = float(all_line[i].split(' ')[2])
    Rvir_h = float(all_line[i].split(' ')[5])
    Rs_h = float(all_line[i].split(' ')[6])

    m_host.append(m_h)
    Rvir_host.append(Rvir_h)
    Rs_host.append(Rs_h)

    Rv = np.array(Rvir_host)
    Rs = np.array(Rs_host)

    s = Rv/Rs


    sub_list = np.array(sub_list)
    m_sub = np.mean(sub_list)

    m_mean_sub.append(m_sub)

   

print(m_host)
print(m_mean_sub)
print(number_sub)
ax[0].plot(m_host,m_mean_sub,'g^')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
#ax[0].set_xlabel('$M_{h}')
ax[0].set_ylabel('$<M_{sh}>$')
ax[1].plot(m_host,number_sub,'rx')
ax[1].set_xscale('log')
#ax[1].set_yscale('log')
ax[1].set_ylabel('$N_{sh}$')
ax[1].set_xlabel(" $M_{vir}^{hh}$")
plt.show()

#for i,ii in enumerate(sub_line):
#    m[i] = float(ii.split(" ")[2])
#
#host_m = float(all_line[int(sub_line[0].split(' ')[-1])].split(' ')[2])
#print(host_m)
#
#fig, ax = plt.subplots()
#ax.hist(np.log10(m))
#ax.hist(np.log10(host_m))
#plt.show()
