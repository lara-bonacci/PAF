import statistics as s

tocke=[]

for n in range(10):
    x=float(input("unesi točku: "))
    tocke.append(x)

print(s.mean(tocke))
print(s.stdev(tocke))