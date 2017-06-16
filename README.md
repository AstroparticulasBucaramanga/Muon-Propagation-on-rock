# Muon Propagation on rock
Here some codes for the propagation of muons in rock. They are used to infer and calculate the flow of muons that cross a structure assuming a flow of incident muons.

To run the **_muonstopping.py_** code, the **_muon_water_dedx.dat_** energy loss data file is needed to generate Bragg curves.

_The graph of specific energy loss (which may be related to specific ionization) along the path of a charged particle is called the Bragg Curve_. To execute the code it is written in the terminal:

> python muonstopping.py

The following two codes generate the muon flux for a specific point of observation and prepare the files to propagate through the mountain and calculate the flux of muons passing through rock. You need the **_muon_2_38.dat_**, **_muon_2_65.dat_**, and **_muon_2_91.dat_** files, and the **_Filtrador_todo.py_** and **_Filtro_sama.py_** codes.

The way to execute them is:

> python Filtrador_todo.py ArchivoSalidaCorsika.out ArchivoResultado_code1.out

This generates a file **_ArchivoResultado_code1.out_** with the information of the muon before passing through rock with format (theta, phi, N). You need the file **_ArchivoSalidaCorsika.out_** which has format (px, p, pz, p) which is the output file of the Corsika simulation with the moments in the three directions and the total momentum of each particle. Then the other propagation code is executed through rock:

> python Filtro_sama.py ArchivoResultado_code1.out ArchivoResultado_code2.out

This generates the flux through rock.
