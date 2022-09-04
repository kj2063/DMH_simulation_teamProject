from pygadgetreader import readrockstar
import numpy as np

_dir = "/home/jun/work_place/astrophysics_project/rockstar-master/dataA_result/"
_file = "halos_0"

pos_arr = readrockstar(_file,"pos")

x = pos_arr[:,0]
y = pos_arr[:,1]
z = pos_arr[:,2]

print(x)
