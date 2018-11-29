import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
import random
import Cellgenerator as cg
from mpl_toolkits.mplot3d import Axes3D
import os
#this imports a lattice as lat from the file, this is the 125
#have to use .cg to things from cellgenerator script!

lat = cg.import_from_file('base.gin',13,1137)

#generates list of Ti and Ba atom sites
Ti_list = lat.singleelement('Ti')
Ba_list = lat.singleelement('Ba')

def randomsample(list):

    sample = range(0, len(list))
    index = random.sample(sample, 30)
    return index
#
# def reduced_list(list,n):
#     out = []
#     for x in list:
#         #print(x.pos)
#         if  not any(y > n for y in x.pos):
#             #print(x.pos)
#             out.append(x.pos)
#     return out
#
# check = [0,0,0]
###### 6 run ran
# reduced_Ti = reduced_list(Ti_list,3.5)
# reduced_Ba = reduced_list(Ba_list, 3)

# new_lat = copy.deepcopy(lat)
# new_lat.replaceatom([1,0,0], 'Er')
# new_lat.replaceatom([1,1,0], 'Er')
# new_lat.replaceatom([0.5, 0.5, 0.5], 'Er')
# new_lat.replaceatom([1.5, 0.5, 0.5], 'Er')

# print(cg.check_charge(new_lat))
#
# cg.genwholefile(new_lat, 'forced2TiEr1', '[0,0,0], [1,0,0], [.5,.5,.5] [1,5,0.5,0.5]')
print(Ti_list)

n=0
num_table = []
while n <= 50:
    new_lat = copy.deepcopy(lat)
    for y in [Ti_list, Ba_list]:
        for x in random.sample(y, 3):
            new_lat.replaceatom(x.pos, 'Er')
            num_table.append(str(n) + ' ' + str(x))

    if cg.check_charge(new_lat) != 0:
        raise Exception('Bad!!!')

    cg.genwholefile(new_lat,'3ofeach'+str(n))
    n +=1
print(Ti_list)
file = open('3ofeach', 'w+')
print(num_table)
for x in num_table:
    file.write(str(x)+'\n')








#print(any(y  for y in check))
