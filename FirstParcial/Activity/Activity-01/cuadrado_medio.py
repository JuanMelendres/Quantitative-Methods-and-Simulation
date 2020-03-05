rnd = input("Ingrese un numero:\n")
length = len(str(rnd))
list = []
while len(list) == len(set(list)) :
    x = str(rnd * rnd)
    if length % 2 == 0:
        x = x.zfill(length * 2)
    else:
        x = x.zfill(length)
    y = (len(x) - length)/2
    rnd = int(x[y:y+length])
    list.append(rnd)
    print(rnd)