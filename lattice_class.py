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
        #adds an atom to the  cell
        self.atoms.append(x)
        return
    def AddFractional(self, pos, type, supercell):
        #adds an atom from fractional coordinates eg. what the gulp files are in
        super_list = [supercell, supercell, supercell]
        lat_pos = np.multiply(pos,super_list)
        self.atoms.append(atom(list(lat_pos), type))
        return

    def getpos(self):
        #generates a list of positions of all the atoms
        out = np.array([[],[],[]])
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
        #changes the type of the atom, wont work if there is no atom there!!
        check = False
        for x in self.atoms:
            if x.pos == v_pos:
                x.type = v_type
                check = True
        if check == False:
            raise Exception('Trying to replace an atom where there is no atom!')

        return
    def addinterstitial(self,i_pos,i_type):
        #adds an atom where there is no atom, will throw an error if you try to
        #add interstitial where there is an atom!!!
        for x in self.atoms:
            if x.pos == i_pos:
                raise Exception('Interstitial placed where atom is!')

        self.add(atom(i_pos, i_type))

        return
    def getdimensions(self):
        #gets the dimensions of the lattice
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
        #generates fractional coordinates
        for x in self.atoms:
            out.append(atom(np.divide(x.pos, max), x.type))
        return out

    def gettype(self, position):
        #returns the type of the atom at that posiition
        for x in self.atoms:
            if x.pos == position:
                return x.type

    def singleelement(self, element):
        #generates a list containing only a single type of atoms
        out =[]
        for x in self.atoms:
            if x.type == element:
                out.append(x)
        return out
