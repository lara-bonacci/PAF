import particle as prt
import numpy as np
import math

p1=prt.Particle(0,0,10,60)

#numerički domet

D=p1.range(0.5)
print(D)       

#p1.plot_trajectory(0.005)

#analitički domet

def domet(x_0,y_0,v,phi):
    v_y=v*np.sin(phi*math.pi/180)
    v_x=v*np.cos(phi*math.pi/180)
    a=-9.81
    t=2*v_y/a
    d=x_0 - v_x*t
    return d

print(domet(0,0,10,60))


odstupanje=abs(D-domet(0,0,10,60))

print("Analitičko rješenje odstupa od numeričkog za {:.4f}".format(odstupanje))