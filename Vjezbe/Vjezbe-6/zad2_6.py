import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import math
import numpy as np


h1=ho.HarmonicOscillator(0.1,10,0.3,0)

#analiticki period

def time_period(m,k):

    T=2*np.pi*math.sqrt(m/k)
    return T

#odstupanje numerickog i analitickog

dt=0
T=[]
a_period=[]
n_period=[]

while dt<=0.05:
    dt+=0.001
    T.append(dt)
    a_period.append(time_period(0.1,10))
    n_period.append(h1.time_period(dt))

print(h1.time_period(0.001))
plt.plot(T,a_period,"r")
plt.scatter(T,n_period,s=3,color="g")
plt.show()

