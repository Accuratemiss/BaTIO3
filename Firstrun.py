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

#adds two Er atoms
lat.replaceatom([0.5,0.5,1.5],'Er')
lat.replaceatom([3.5,3.5,3.5],'Er')

#generates a list of O atoms
Olist =lat.singleelement('O')

#generates an list from 1-375 to pick 50 sites ty try O atom
samplearray = range(0,len(Opos))

#random 50 sites to try
index = random.sample(samplearray,50)
n=0
for x in index:
    #copy the lattice to stop any weirdness
    new_lat = copy.deepcopy(lat)
    #Olist contains atoms, so .pos get the position out of Olist
    #replaces O with vacanty
    new_lat.replaceatom(Olist[x].pos,'O_v')
    cg.genwholefile(new_lat, '2Er1Ovac'+' '+ str(n))
    n+=1



#print(lat.getpositions())
