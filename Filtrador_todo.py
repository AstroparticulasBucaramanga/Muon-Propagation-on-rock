# ------- creado por Martha Valencia -------

# python Filtrador_final_muones_momentum.py datosmuones.out salida.out
# Este codigo imprime momentum y la cantidad de muones por angulo azimuth,zenith para el angulo de apertura dado por el telescopio, en pasos de 1 grado
# Ejemplo: azimuth, zenith - 1, 60 - 1, 61 .... 5, 60 - 5, 61 .....60, 60 - 60, 61

import math
import sys

file0 = sys.argv[1] #archivo que contiene los datos
file1 = sys.argv[2] #archivo donde se escriben los datos

gdata = open(file1+".out", 'w')

for readline in open(file0):
    row = readline.split( )
#    if row[3] == "0":
#	print "aqui"
    if row[0] != "#" and row[3] != "0":
        if float(row[0]) > 0.0 and float(row[1]) >= 0.0:
            phir = math.atan(float(row[1])/float(row[0]))
        if float(row[0]) > 0.0 and float(row[1]) <= 0.0:
            phir = 2*math.pi + math.atan(float(row[1])/float(row[0]))
        if float(row[0]) < 0.0 and float(row[1]) >= 0.0:
            phir = math.pi + math.atan(float(row[1])/float(row[0]))
        if float(row[0]) < 0.0 and float(row[1]) <= 0.0:
            phir = math.pi + math.atan(float(row[1])/float(row[0]))
	if float(row[0]) == 0.0 and float(row[1]) > 0.0:
	    phi = 90
	if float(row[0]) == 0.0 and float(row[1]) < 0.0:
 	    phi = 270
        phi = math.degrees(phir) # phi es angulo azimutal en grados y phir es radianes        
        thetar = math.acos(float(row[2])/math.sqrt(float(row[0])*float(row[0])+float(row[1])*float(row[1])+float(row[2])*float(row[2]))) #ar es angulo cenital en radianes
        theta = math.degrees(thetar) #a es angulo cenital en grados
 	gdata.write("%s %d %d\n"%(row[3], int(round(theta,0)), int(round(phi,0))))        
