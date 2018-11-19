import numpy as np
import copy

class atom(object):
    """defines an atom/vancancy with the properties
    of position and type .
            pos = position of atom in lattice space
            type = type of atom/vacanvy in space"""
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
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

    def getpos(self):
        #generates a list of positions of all the atoms
        out = []
        for x in self.atoms:
            out.append(x.pos)
        return out

    def realpos(self):
        #generates a real position from lattice parameter and crystal direction
        out = []
        for x in self.getpos():
            mul = np.multiply(x, self.lp)
            out.append(mul)
            return out
    def genvacancy(self,v_pos,v_type):
        #generates a vacancy and checks the type of atom on that site
        #v_pos is the vacancy position
        n = 0
        for x in self.atoms:
            if x.pos == v_pos:
                if x.type == v_type:
                    x.type = x.type + '_v'
                    n = n+1
                else:
                    pass
                    #add error handling here
                    #except('Oops there is more than one atom on that site!')
        return
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


    def genfractional(self):
        out=[]
        max = self.getdimensions()
        for x in self.atoms:
            out.append(atom(np.divide(x.pos, max), x.type))
        return out


#Generated BaTio4 cell
# lat = lattice([Ba((0,0,0)),Ba((1,0,0))], (4,4,4))
#
# new = Ba((1,1,1))
# lat.add(new)

###Maybe dont touch
def makecell():
    #initialises a BaTiO3 unit makecell
    #soz for the global variable, bad James
    global lat
    lat = lattice([],(4,4,4))
    new = atom((0,0,0),'Ba')
    # lat.add(Ba(new))
    for x in [(0,0,0),(1,0,0),(0,0,1),(0,1,0),(1,1,0),(0,1,1),(1,0,1),(1,1,1)]:
        new = atom(x, 'Ba')
        lat.add(new)
    for x in [(.5,.5,0),(0,.5,.5),(.5,0,.5),(.5,.5,1),(1,.5,.5),(.5,1,.5,)]:
        new = atom(x, 'O')
        lat.add(new)
    new = atom((.5,.5,.5),'Ti')
    lat.add(new)
    return

makecell()
####
def supercell(lat,n):
    #generates nxnxn supercell
    #programming gods please dont get pissy about me copy and pasting
    ogatoms = copy.deepcopy(lat.atoms)
    for x in range(1,n):
        for y in ogatoms:
            #x direction
            #if statements exclude atoms at 0 as they will place atoms as
            #existing poinsts
            if y.pos[0] == 0:
                pass
            else:
                newpos = np.add(y.pos, (x, 0, 0))
                lat.add(atom(newpos,y.type))
    ogatoms = copy.deepcopy(lat.atoms)
    for x in range(1,n):
        for y in ogatoms:
            #y direction
            if y.pos[1] == 0:
                pass
            else:
                newpos = np.add(y.pos, (0, x, 0))
                lat.add(atom(newpos,y.type))
    ogatoms = copy.deepcopy(lat.atoms)
    for x in range(1,n):
        for y in ogatoms:
            if y.pos[2] == 0:
                pass
            else:
                newpos = np.add(y.pos, (0, 0 , x))
                lat.add(atom(newpos,y.type))

    return lat

###test code###
lat = supercell (lat,5)
# lat.geninterstitial((0.1,0.1,0),'O')
# max = [0,0,0]


# for x in lat.genfractional():
#     print(str(x.pos) + ' ' + str(x.type))
# atomdict = {'Ba':'Ba  core '}
# test = 5.24242424
# a = 'a'
# b = 'a'
#genericstring1 = '{:.3f} {:.3f}'.format(test,test) #
##def gencode(lat):
#print(genericstring1)
corevalues = {'Ba':[3.45,1,0],
              'Ti':[4,1,0],
              'O':[0.472,1,0],
              'Er':[3.451,1,0]}
shellvalues = {'Ba':[-1.45,1,0],
                'O':[-2.472,1,0]}
def gencode(lat,out):
    #takes a lattice and generates an output file
    (c,d,e) = (1,1,1)

    file = open(out,'w+')
    for x in lat.genfractional():
        if x.modeltype() == 'coreshell':
            genericstring1 = '{:2}    {:>4} {:.7f} {:7f} {:7f} {:.8f} {:.5f} {:.5f} \n'.format(x.type,'core', x.pos[0],x.pos[1],x.pos[2],corevalues[x.type][0],corevalues[x.type][1],corevalues[x.type][2])
            file.write(genericstring1)
            genericstring1 = '{:2}    {:>4} {:.7f} {:7f} {:7f} {:.8f} {:.5f} {:.5f} \n'.format(x.type,'shel', x.pos[0],x.pos[1],x.pos[2],shellvalues[x.type][0],shellvalues[x.type][1],shellvalues[x.type][2])
            file.write(genericstring1)
        else:
            genericstring1 = '{:2}    {:>4} {:.7f} {:7f} {:7f} {:.8f} {:.5f} {:.5f} \n'.format(x.type,'core', x.pos[0],x.pos[1],x.pos[2],corevalues[x.type][0],corevalues[x.type][1],corevalues[x.type][2])
            file.write(genericstring1)

    return
def genwholefile()

gencode(lat,'testing.txt')

print(lat.atoms[1].modeltype())
