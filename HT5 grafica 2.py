#Created on 2020
#@author: Dulce Calán

import numpy as np
import matplotlib.pyplot as plt
import math as m

def x(t):
    C = 0
    A = 2
    B = 4
    Ao = 10
    beta = 0.1
    wo = 1
    w1 = m.sqrt(wo**2 - beta**2)
    return (A+B*t)*m.exp(-beta*t)+C

# SE CREAN ARRELGOS
'''el primer arreglo define cuantos puntos de tiempo se van a valuar
y el segundo es un arreglo conformado por ceros que luego seran sustituidos
por el valor de la funcion para ese instante de tiempo'''
t = np.linspace(0,50,100)
r = np.zeros(len(t))

# SE VALUA LA FUNCION (tomando cada tiempo, valuandolo y sustituyendolo en el
# segundo arreglo)
for i in range(len(t)):
    r[i] = x(t[i])

# SE PLOTEA
# grafica la funcion en color negro y una linea continua
plt.plot(t,r,'-k',label='$x(t)$')
# muestra la leyenda dada por 'label' en el comando pasado
plt.legend()
# nombres de cada uno de los ejes
plt.xlabel('Tiempo')
plt.ylabel('Posicion')
plt.grid()
# titulo del grafico
plt.title('Problema 1 Amortiguamiento critico con F  igua a 0')
# nombre y extencion de la grafica (se guarda en la carpeta donde este el prog.)
plt.savefig('problema 1 HT1_1.pdf')
# se muestra la grafica
plt.show()
