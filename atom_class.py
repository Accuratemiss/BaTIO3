import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class atom(object):
    """defines an atom/vancancy with the properties
    of position and type .
            pos = position of atom in lattice space
            type = type of atom/vacanvy in space"""
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type

    def __str__(self):
        return 'position:'str(self.pos) +  ' type:'self.type

    def properties(self):
        charges = {'Ba':2,
                   'O':-2,
                   'Ti':4,
                   'Ti3':3,
                   'O_v':2,
                   'Ba_v':-2,
                   'Ti_v':-4,
                   'Ti3_v':-3}

        return charges[self.type]

    def modeltype(self):
        types = {'Ba':'coreshell',
                   'O':'coreshell',
                   'Ti':'core',
                   'Er':'core'}
        return types[self.type]
