# ------- creado por Martha Valencia -------

# python Filtrador_sama.py salidarealvolcan.out salidatotalvolcan.out
# Este codigo filtra los muones simulados con corsika para encontrar cuales atraviesan una estructura geologica

import sys

file1 = sys.argv[1] # entrada que contiene los datos de salida del corsika ... Momentum Theta Phi 
file2 = sys.argv[2] # salida ... Phi Theta #muones

auxdata1 = open('muon_2_65.dat', 'r') # distancias que atraviesan los muones con momentum inicial
auxdata2 = open('distp1_machin.dat', 'r') # distancias que atraviesan los muones en la topografia de la estructura

amin = 117 # angulo azimutal minimo se cuenta desde el norte
amax = 147 # angulo azimutal maximo se cuenta desde el norte
cmin = 66 # angulo cenital minimo
cmax = 84 # angulo cenital maximo

crange = cmax-cmin
if amax > amin:
    arange = amax-amin
if amin > amax:
    arange = 360-amin+amax

#-----------Leyendo la data auxiliar-----------------------------------------------------------
print "Leyendo la data auxiliar..."
distreal = [[0 for m in range(arange+1)] for n in range(crange+1)]
dp = []
dr = []

for readline in auxdata1:
    x = readline.split()
    if x[0] != "#":
        dp.append(x[0]) #guarda en el arreglo dp el momentum de la particula
        dr.append(x[3]) #guarda en dr la distancia que recorre la particula que tiene ese momentum guardado en dp

for readline in auxdata2:
    row = readline.split()
    if row[0] != '#':
        n = int(row[1]) - cmin
        m = int(row[0]) - amin
        if m < 0:
            m = 360 - amin + int(row[0])
        distreal[n][m] = float(row[2]) # guarda en distreal las distancias atravesadas en la topografia para cada direccion de arribo

#-----------Ordenando particulas por momentum--------------------------------------------------
print "Ordenando muones por momentum..."

energy = {'momentum': 'angle'}
l = 0

test = []
test.append('momentum')
for readline in open(file1):
    row = readline.split( )
    if l == 1:
        del energy['momentum']
        l = 2
    if cmin <= int(row[1]) <= cmax:
        p = 0
        if (amax > amin and amin <= int(row[2]) <= amax) or ((amin>amax and amin <= int(row[2])) or (amin>amax and amax >= int(row[2]))):
            def admuones():
                if amax > amin:
                    for i in range(amin, amax+1):
                        for j in range(cmin, cmax+1):
                            if i == int(row[2]) and j == int(row[1]):
                                m = i - amin
                                n = j - cmin
                                energy[key1][n][m] = energy [key1][n][m] + 1
                                break
                if amin > amax:
                    for j in range(cmin, cmax+1):
                        for i in range(amin, 360+1):
                            if i == int(row[2]) and j == int(row[1]):
                                m = i - amin
                                n = j - cmin
                                energy[key1][n][m] = energy[key1][n][m] + 1
                                break
                        for i in range(0, amax+1):
                            if i == int(row[2]) and j == int(row[1]):
                                m = (360-amin) + i
                                n = j - cmin
                                energy[key1][n][m] = energy[key1][n][m] + 1
                                break
            key1 = str(row[0])
            for obj in test:    
                if key1 == obj:
                    admuones()
                else:
                    p = p+1
            if p == len(test):
                energy[key1] = [[0 for m in range(arange+1)] for n in range(crange+1)]
                admuones()
                test.append(key1)
                if l == 0: l = 1

#-----------Filtrando las particulas que atraviesan la estructura------------------------------              
print "Filtrando particulas..."
dist = [[0 for m1 in range(arange+1)] for n1 in range(crange+1)]
sorted(energy)
for key in energy:
    r = len(dp) - 1 #cambio de indice
    while (r >=0 and float(key) < float(dp[r])): #compara el momentum de las particulas simuladas, con aquel de los muones en roca
        r -=1
    if (r < 0 or r == 0):
        r = 0
    for j in range(cmin, cmax+1):
        n1 = j - cmin
        if amax > amin:
            for i in range(amin, amax+1):
                m1 = i - amin
                if energy[key][n1][m1] != 0 and float(dr[r]) >= distreal[n1][m1]:
                    dist[n1][m1] = dist[n1][m1] + energy[key][n1][m1]
        if amin > amax:
            for i in range(amin, 360+1):
                m1 = i - amin
                if energy[key][n1][m1] != 0 and float(dr[r]) >= distreal[n1][m1]:
                    dist[n1][m1] = dist[n1][m1] + energy[key][n1][m1]
            for i in range(1, amax+1):
                m1 = (360-amin) + i
                if energy[key][n1][m1] != 0 and float(dr[r]) >= distreal[n1][m1]:
                    dist[n1][m1] = dist[n1][m1] + energy[key][n1][m1]
                                  
#-----------Print Final------------------------------
print "Imprimiendo..."
adata = open(file2+".out", 'w') #archivo donde se escriben los datos de muones que atraviesan la topografia en las direcciones dadas por los rangos angulares
adata.write("# Filtracion de muones para rango azimutal(Phi) entre %d y %d grados \n"%(amin, amax))
adata.write("# Filtracion de muones para rango cenital(Theta) entre %d y %d grados \n"%(cmin, cmax))
adata.write("# Ang_azimutal Ang_cenital #Muones\n")
for j in range(cmin, cmax+1):
    n = j - cmin
    if amax > amin:
        for i in range(amin, amax+1):
            m = i - amin
            adata.write("%d %d %d\n"%(i, j, dist[n][m]))                
    if amin > amax:
        for i in range(amin, 360+1):
            m = i - amin
            adata.write("%d %d %d\n"%(i-360, j, dist[n][m]))                
        for i in range(0, amax+1):
            m = 360 - amin + i
            adata.write("%d %d %d\n"%(i, j, dist[n][m]))                
    adata.write('\n')
