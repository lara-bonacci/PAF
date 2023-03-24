import numpy as np
import math
import matplotlib.pyplot as plt
import statistics as s


M= np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi= np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

D=M/phi

a=s.mean(M*phi)/s.mean(phi**2)
y=a*phi
error=math.sqrt((s.mean(M**2)/s.mean(phi**2)-a**2)/len(M))

print("Modul torzije aluminijske šipke: {}".format(D))
print("Standardna pogreška procjene iznosi {}".format(error))

plt.scatter(phi,M)
plt.plot(phi,y)
plt.xlabel("\u03C6 [rad]")
plt.ylabel("M [Nm]")
plt.title("linearna regresija")
plt.show()