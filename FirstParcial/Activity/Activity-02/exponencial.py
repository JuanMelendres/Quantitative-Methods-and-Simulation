import matplotlib.pyplot as plt
from random import randint
import math

data = []

def exponencial_inversa(u_value):
    lmbda = 1.5
    return -(math.log(1-u_value)/lmbda)

for i in range (10000):
    r = randint(1,99)/100
    data.append(exponencial_inversa(r))

plt.hist(data, bins = 50)
plt.title("Exponencial")
plt.show()