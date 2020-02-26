import numpy as np
import matplotlib.pyplot as plt

# Funcion para tranformar 
def box_muller(u1,u2):
  x1 = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
  x2 = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
  return x1,x2

# Valores entre 0 y 1
u1 = np.random.rand(10000)
u2 = np.random.rand(10000)

# Llamamos la funcion
a,b = box_muller(u1,u2)

# Graficando los valores antes y despues de la tranformacion
plt.figure()
# Valores sin tranformar
plt.subplot(221)
plt.hist(u1)     
plt.subplot(222)
plt.hist(u2)
# Valores con tranformacion
plt.subplot(223)
plt.hist(a)
plt.subplot(224)
plt.hist(b)
plt.show()