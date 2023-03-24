import statistics as s
import math as m

tocke=[]

for n in range(10):
    x=float(input("unesi točku: "))
    tocke.append(x)

print(s.mean(tocke))
print(s.stdev(tocke)/m.sqrt(len(tocke)))