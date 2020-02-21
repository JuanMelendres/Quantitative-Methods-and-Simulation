a = int(input("Ingrese 'a': "))
c = int(input("Ingrese 'c': "))
X0 = int(input("Ingrese el valor del seed: "))
m = int(input("Ingrese 'm: "))
g2 = m + 2
print("Los numeros random: ")
g1 = ((a * X0) + c) % m
print(X0)
print(g1)
if(m > 0 and a > 0 and a < m and c >= 0 and c < m and X0 >= 0 and X0 < m):
	while(g2 != X0):
	  g2 = ((a * g1) + c) % m
	  print(g2)
	  g1 = g2 