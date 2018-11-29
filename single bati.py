import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
import random
import Cellgenerator as cg
from mpl_toolkits.mplot3d import Axes3D

#this imports a lattice as lat from the file, this is the 125
#have to use .cg to things from cellgenerator script!

lat = cg.import_from_file('base.gin',13,1137)
#generates list of Ti and Ba atom sites
Ti_list = lat.singleelement('Ti')
Ba_list = lat.singleelement('Ba')

lat.replaceatom([0,0,0], 'Er')

coord_list = []
for x in Ti_list:
    if x.pos[0] == 0.5:
        coord_list.append(x.pos)
n = 0
for x in coord_list:
    new_lat = copy.deepcopy(lat)
    new_lat.replaceatom(x, 'Er')
    if cg.check_charge(new_lat) != 0:
        raise Exception('Not charge neutral!')
    cg.genwholefile(new_lat, 'Firstru_TiBa.gin' +str(n), '# Ba [0, 0, 0]' + str(x))
    n += 1
