import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
import random
import Cellgenerator as cg
from mpl_toolkits.mplot3d import Axes3D
import os
import atom_class
#this imports a lattice as lat from the file, this is the 125
#have to use .cg to things from cellgenerator script!

lat = cg.import_from_file('base.gin',13,1137)

#generates list of Ti and Ba atom sites
Ti_list = lat.singleelement('Ti')
Ba_list = lat.singleelement('Ba')
O_list = lat.singleelement('O')

# def randomsample(list):
#
#     sample = range(0, len(list))
#     index = random.sample(sample, 30)
#     return index
#
n=1
num_runs = 50
num_table = []
name = '1Ti_2Ba_1Ov'
while n <= num_runs:
    new_lat = copy.deepcopy(lat)

    Ba_sites = random.sample(Ba_list, 1 )
    Ti_sites = random.sample(Ti_list, 3)
    O_sites = random.sample(O_list, 1)

    Ertest = atom_class.atom([0,0,0], 'Er')

    for x in Ba_sites:
        new_lat.replaceatom(x.pos,'Er')
        num_table.append(str(n) + ' ' + str(x) + ' ' + str(x.type))

    for x in Ti_sites:
        print('yo')
        new_lat.replaceatom(x.pos, 'Er')
        num_table.append(str(n) + ' ' + str(x) + ' ' + str(x.type))

    for x in O_sites:
        new_lat.replaceatom(x.pos, 'O_v')
        num_table.append(str(n) + ' ' + str(x) + ' ' + str(x.type))

    print(cg.check_charge(new_lat))
    for x in ['Ba', 'Er', 'Ti', 'O']:
        print(x, len(new_lat.singleelement(x)))
    cg.genwholefile(new_lat, name + str(n))
    n += 1

file = open(name + 'pos', 'w+')
for x in num_table:
    file.write(str(x)+'\n')








#print(any(y  for y in check))
