rnd = input("Ingrese un numero: \n")
rnd2 = input("Ingrese un numero: \n")
length = len(str(rnd))
length2 = len(str(rnd2))
list = []
while len(list) == len(set(list)) :
    x = str(rnd * rnd)
    y = str(rnd2 * rnd2)
    if length % 2 == 0 and length2 % 2 == 0:
        x = x.zfill(length * 2)
        y = y.zfill(length2 * 2)
    else:
        x = x.zfill(length)
        y = y.zfill(length2)
    z = (len(x) - length)/2
    rnd = int(x[y:y+length])
    list.append(rnd)
    print rnd