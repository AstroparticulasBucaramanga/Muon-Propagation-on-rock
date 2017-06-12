# Propagacion de Muones en Roca
Acá unos códigos para la propagación de muones en roca. Se usan para inferir y calculas el flujo de muones que atraviesan una estructura asumiendo un flujo de muones incidentes.

Para ejecutar el código **_muonstopping.py_** se neecsita el archivo de datos de pérdidas de energas **_muon_water_dedx.dat_** para generar unas curvas de Bragg. 

La gráfica de la pérdida de energía específica (que puede estar relacionada con la ionización específica) a lo largo de la trayectoria de una partícula cargada se denomina Curva de Bragg. Para ejecutar el código se escribe en la terminal:

> python muonstopping.py

Los siguientes dos códigos generan el flujo de muones para un punto específico de observación y preparan los archivos para propagar a través de la montaña y calcular el flujo de muones que pasan a través de roca. Se necesitan los archivos **_muon_2_38.dat_**, **_muon_2_65.dat_** y **_muon_2_91.dat_** y los códigos **_Filtrador_todo.py_** y **_Filtro_sama.py_**.

La forma de ejecutarlos es:

> python Filtrador_todo.py ArchivoSalidaCorsika.out ArchivoResultado_code1.out

Esto genera un archivo **_ArchivoResultado_code1.out_** con la información del flujo de muones antes de pasar por roca con formato _(theta,phi,N)_. Se neecsita el archivo **_ArchivoSalidaCorsika.out_** el cual tiene formato _(px,py,pz,p)_ que es el archivo de salida de la simulación de Corsika con los momentos en las tres direcciones y el momento total de cada partícula. Luego se ejecuta el otro código de propagación a través de roca:

> python Filtro_sama.py ArchivoResultado_code1.out ArchivoResultado_code2.out

Esto general el flujo a través de roca.
