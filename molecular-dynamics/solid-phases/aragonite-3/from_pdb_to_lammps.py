import numpy as np
import ase.io
from ase.calculators.espresso import Espresso
import os

conf=ase.io.read('aragonite.pdb')
new_species=np.array(conf.get_chemical_symbols())
print(new_species)
new_species[new_species=='Ca']='Al'
new_species[new_species=='C']='B'
new_species[new_species=='O']='Dy'
new_species[new_species=='H']='F'
conf.set_chemical_symbols(new_species)
ase.io.write('caco3.lammps-data',conf, format='lammps-data')
