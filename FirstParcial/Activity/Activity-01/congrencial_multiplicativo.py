a = int(input("Ingrese 'a': "))
seed = int(input("Ingrese el valor del seed: "))
m = int(input("Ingrese 'm: "))
g2 = m + 2
print("Los numeros random: ")
g1 = (a * seed) % m
print(seed)
print(g1)
if(m > 0 and a > 0 and a < m  and seed >= 0 and seed < m):
	while(g2 != seed):
	  g2 = (a * g1) % m
	  print(g2)
	  g1 = g2 