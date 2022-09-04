from pygadgetreader import readrockstar
import numpy as np
import matplotlib.pyplot as plt
import heapq

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"

m_vir = readrockstar(_dir+_file,"m")

a = open(_dir+"box25_parent.log", "r")
sub_line = a.readlines()[16:]

host_arr = []
sub_arr = []

b = open(_dir+"out_0.list", "r")
all_line = b.readlines()[16:]


for l in sub_line:
    if l.split(" ")[-1] == "-1\n":
        host_arr.append(l)

for l in sub_line:
    if l.split(" ")[-1] != "-1\n":
        sub_arr.append(l)

host_sub = np.zeros(len(all_line))
count = np.zeros(len(all_line))

for ii,i in enumerate(all_line):
    for j in sub_arr:
        if int(i.split(" ")[0]) == int(j.split(" ")[-1]):
            count[ii] += 1

count = list(count)
print(count[8307],count[8152])

#30 = the number of data
num_list = heapq.nlargest(30, xrange(len(count)), key=count.__getitem__)


fig, ax = plt.subplots(2)

m_mean_sub = []
m_host = []
number_sub = []


for i in num_list:
    sub_list = []

    for j in sub_line:
        if i == int(j.split(' ')[-1]):
            sub_list.append(float(j.split(' ')[2]))

    number_sub.append(len(sub_list))

    print(len(sub_list))
    m_h = float(all_line[i].split(' ')[2])

    m_host.append(m_h)

    sub_list = np.array(sub_list)
    m_sub = np.mean(sub_list)

    m_mean_sub.append(m_sub)



print(m_host)
print(m_mean_sub)
print(number_sub)
ax[0].plot(m_host,m_mean_sub,'g^')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_ylabel('Mean Mass of Sub_Halos')
ax[1].plot(m_host,number_sub,'rx')
ax[1].set_xscale('log')
ax[1].set_yscale('log')

