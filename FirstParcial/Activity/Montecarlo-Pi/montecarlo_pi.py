import random as rnd
import math as math

total = 2000000 #1000000

def montecarlo(t):
    inside = 0
    pi = 0
    for i in range(0, t):
        x2 = rnd.random()**2
        y2 = rnd.random()**2
        if math.sqrt(x2 + y2) < 1.0:
            inside += 1
    
    pi = (float(inside) / t) * 4
    return pi

print(montecarlo(total))