import harmonic_oscillator as ho
import numpy as np
import matplotlib.pyplot as plt
import math

h1=ho.HarmonicOscillator(0.1,10,0.3,0)

h1.plot_trajectory(2,0.0001)


#numerički pomak
def numeric(dt,color,size):
    
    plt.scatter(h1.oscillate(2,dt)[3],h1.oscillate(2,dt)[2],s=size,c=color,label="dt={}".format(dt))

#analitički pomak
def analytical(m,k,A):
    T_a=np.arange(0,2,0.0001)
    X_a=[]

    for t_a in T_a:
        x_a=A*np.cos(math.sqrt(k/m)*t_a)
        X_a.append(x_a)

    plt.plot(T_a,X_a,color="r",label="analytical")
    

analytical(0.1,10,h1.amplitude(0.0001))
numeric(0.001,"g",1)
numeric(0.01,"orange",3)
numeric(0.05,"b",5)

plt.legend()
plt.show()









