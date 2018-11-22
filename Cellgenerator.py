import numpy as np
import copy
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from atom_class import atom
from lattice_class import lattice

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
lat = lattice([],[4,4,4])
element_tags = ['Ba', 'O ', 'Ti']

def extract_pos(line, element):
    x_start = line.find('core ') + 5
    if x_start == 4:
        if line.find('shel ') != -1:
            return 'shel'
        else:
            print('Bad Stuff!!')
    else:
        pos_out= []
        x_end = line.find(' ', x_start)
        pos_out.append(float(line[x_start:x_end]))
        y_start = x_end + 1
        print(y_start)
        y_end = line.find(' ', y_start)
        pos_out.append(float(line[y_start:y_end]))
        z_start = y_end + 1
        z_end = line.find(' ', z_start)
        pos_out.append(float(line[z_start:z_end]))
    return pos_out


def import_from_file(path,start,stop):
    #copy pasted soz guys, little bit of a bodge
    out = lattice([], [4,4,4])

    ### opens fiileas a list containing each line as a value
    def openfile(filename):
        with open(path, "r") as f:
            all_lines = f.readlines()
        return all_lines
    data = openfile(path)

    data_slice = data[start:stop]
    #print(data_slice)
    n = float(start)
    for x in data_slice:
        if x.find('#') == -1:
            for element in element_tags:
                if x[0:2] == element:
                    coords = extract_pos(x, element)
                    if coords == 'shel':
                        pass
                    else:
                        print(coords)
                        if element == 'O ':
                            out.AddFractional(coords, 'O', 5)
                        else:
                            out.AddFractional(coords, element, 5)
                            n = n+1
                        print(n)
        else:
            pass


    return out

lat = import_from_file('BaTiO3125.gin',13,1137)
n = 0


corevalues = {'Ba':[3.45,1,0],
              'Ti':[4,1,0],
              'O':[0.472,1,0],
              'Er':[3.451,1,0]}
shellvalues = {'Ba':[-1.45,1,0],
                'O':[-2.472,1,0]}
def gencode(lat):
    #takes a lattice and generates an output file called temp.txt
    (c,d,e) = (1,1,1)

    file = open('temp.txt','w+')
    for x in lat.genfractional([5,5,5]):
        print (x.pos)
        if x.type[-2:] != '_v':
            if x.modeltype() == 'coreshell':
                genericstring1 = '{:2}    {:>4} {:.7f} {:7f} {:7f} {:7.8f} {:.5f} {:.5f} \n'.format(x.type,'core', x.pos[0],x.pos[1],x.pos[2],corevalues[x.type][0],corevalues[x.type][1],corevalues[x.type][2])
                file.write(genericstring1)
                genericstring1 = '{:2}    {:>4} {:.7f} {:7f} {:7f} {:9.7f} {:.5f} {:.5f} \n'.format(x.type,'shel', x.pos[0],x.pos[1],x.pos[2],shellvalues[x.type][0],shellvalues[x.type][1],shellvalues[x.type][2])
                file.write(genericstring1)
            else:
                genericstring1 = '{:2}    {:>4} {:.7f} {:7f} {:7f} {:.8f} {:.5f} {:.5f} \n'.format(x.type,'core', x.pos[0],x.pos[1],x.pos[2],corevalues[x.type][0],corevalues[x.type][1],corevalues[x.type][2])
                file.write(genericstring1)

    return

def genwholefile(lat,out):
    gencode(lat)
    file = open(out,'w+')
    preamble = open('preamble','r')
    temp = open('temp.txt', 'r')
    postamble = open('postamble','r')
    try:
        file.write(prelude)
    except:
        print('No prelude')
        pass
    file.write(preamble.read())
    file.write(temp.read())
    file.write(postamble.read())

def plotter():
    fig = plt.figure()
    print(lat.getpos()[0])
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter()
    plt.show()

#genwholefile(lat,'asdk;jfhasfha')
gencode(lat)
print('good stuff')
