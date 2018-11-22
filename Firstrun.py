import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
import Cellgenerator as cg
from mpl_toolkits.mplot3d import Axes3D
from atom_class import atom
from lattice_class import lattice

#import BaTiO3 base cell 5x5x5
lat = cg.import_from_file('BaTiO3125.gin',13,1137)
charge = 0
for x in lat.atoms:
    charge += x.properties()
print (charge)
