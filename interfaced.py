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

n=1
num_runs = input('Please enter the number of runs: ')
num_runs = int(num_runs)

name = input('Please enter the name of your files: ')

mech1 = input('Please enter the number of mech1 instances: ')
mech1 = int(mech1)

mech2 = input('Please enter the number of mech2 instances: ')
mech2 = int(mech2)

num_table = []


def mech_Ti_Ba(Ba_sites, Ti_sites):
    #carries out Ti/Ba substitution
    for x in Ba_sites:
        for x in Ba_sites:
            new_lat.replaceatom(x.pos,'Er')
            num_table.append(str(n) + ' ' + str(x) + ' ' + str(x.type))

        for x in Ti_sites:
            lat.replaceatom(x.pos, 'Er')
            num_table.append(str(n) + ' ' + str(x) + ' ' + str(x.type))
        return

def mech_Ti_Ov(Ti_sites, O_sites):
    for x in Ti_sites:
        new_lat.replaceatom(x.pos, 'Er')
        num_table.append(str(n) + ' ' + str(x) + ' ' + str(x.type))
    for x in O_sites:
        lat.replaceatom(x.pos, 'O_v')
    return




while n <= num_runs:
    new_lat = copy.deepcopy(lat)

    Ba_num = copy.copy(mech1)
    Ba_master = random.sample(Ba_list, Ba_num)

    Ti_num = mech1 + (2 * mech2)
    Ti_master = random.sample(Ti_list, Ti_num)

    O_num = copy.copy(mech2)
    O_master = random.sample(O_list, O_num)

    if not mech1 == 0:
        mech_Ti_Ba(Ba_master[0:mech1 - 1], Ti_master[0: mech1-1])

    if not mech2 == 0:
        mech_Ti_Ov(Ti_master[mech1:], O_master)

    cg.genwholefile(new_lat, name + str(n))
    n += 1

file = open(name + 'pos', 'w+')
for x in num_table:
    file.write(str(x)+'\n')
