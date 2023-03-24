import math as math
tocke=[]

for n in range(10):
    x=float(input("unesi točku: "))
    tocke.append(x)

def aritematicka_sredina(podaci):
    suma=0
    for i in podaci:
        suma+=i
    a=suma/len(podaci)
    return a

def devijacija(podaci):
    suma=0
    for i in podaci:
        suma+=(i-aritematicka_sredina(podaci))**2
    d=math.sqrt(suma/(len(podaci)-1))
    return d

print(aritematicka_sredina(tocke))
print(devijacija(tocke))