import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from atom_class import atom

class lattice(object):
    """contains atoms is a list of all the atoms stored as lattoce
    vectors and a lattice parameters
            atoms = list of all atoms/vacancies/
            lp = lattice parameters of unit cell"""
    def __init__(self, atoms, lp):
        self.atoms = atoms
        self.lp = lp

    def add(self,x):
        #adds an atom to the unit cell
        self.atoms.append(x)
        return
    def AddFractional(self, pos, type, supercell):
        #adds an atom with fractional coordinates
        super_list = [supercell, supercell, supercell]
        lat_pos = np.multiply(pos,super_list)
        self.atoms.append(atom(lat_pos, type))
        return

    def getpos(self):
        #generates a list of positions of all the atoms
        out = self.atoms[0].pos
        print(out)
        for x in self.atoms[1:]:
            np.append(out, x.pos, axis = 0)
        return out

    def realpos(self):
        #generates a real position from lattice parameter and crystal direction
        out = []
        for x in self.getpos():
            mul = np.multiply(x, self.lp)
            out.append(mul)
            return out
    def replaceatom(self,v_pos,v_type):
        #generates a vacancy and checks the type of atom on that site
        #v_pos is the vacancy position
        n = 0
        for x in self.atoms:
            if x.pos == v_pos:
                if x.type == v_type:
                    x.type = x.type + '_v'
                    n = n+1
                else:
                    raise Exception('tried to replace atom when atom did not exist')

    def geninterstitial(self,i_pos,i_type):
        for x in self.atoms:
            if x.pos == i_pos:
                #error
                pass

        self.add(atom(i_pos,i_type))
        return
    def getdimensions(self):
        max = [0,0,0]
        for x in self.atoms:
            if x.pos[0] > max[0]:
                max[0] = x.pos[0]
        # for x in self.atoms:
            if x.pos[1] > max[1]:
                max[1] = x.pos[1]
            else:
                pass
            if x.pos[2] > max[2]:
                max[2] = x.pos[2]
        return max


    def genfractional(self,max):
        out=[]
        # max = self.getdimensions()
        for x in self.atoms:
            out.append(atom(np.divide(x.pos, max), x.type))
        return out
