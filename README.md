# BaTIO3
Writing code with my code.

There are two classes in this code, the atom class, and the lattice class.
Classes behave a little like a function and a little like an object.

An atom has two properties. It's position and its type.
To make a barium atom as a variable called Bar at a position (0,0,1)
You use the code:
	Bar = atom([0,0,1], 'Ba')

That simple!

To get the position you use Bar.pos, to get the type you use Bar.type

A lattice has two parameters a list of the atoms it contains, and a set of
lattice parameters.
To make a lattice called lat, with the atom Bar in you just type (and lattice parameters [4,4,4]

	lat = lattice([Bar], [4,4,4]))

Methods!!

sometimes the data in a lattice is in the wrong form, this is where methods come

 in, a method runs a function on the data in the lattice
e.g.

when using a method, like a function it has to have brackets, even if there is no input

e.g. lat.getfractional()

lat.replaceatom([coords to replavec] , 'replacement type')

A word on the classes.
If you get something like this out
<atom_class.atom object at 0x08BCF6B0>, <atom_class.atom object at 0x08BCF890>, <atom_class.atom object at 0x08BCF8B0>,
you havent gone deep enough if that makes sense. You are printing the container not the numbers themselves.

If you print lat.atoms[0].pos you will get the posisitions. THis is because you open the lat.atoms container. Which is a list
The [0] goes to the first item in the list, then .pos accesses the positions.
