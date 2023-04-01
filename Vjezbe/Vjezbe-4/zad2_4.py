import particle as prt
import numpy as np
import math
import matplotlib.pyplot as plt

p1=prt.Particle(0,0,10,60)

def domet(x_0,y_0,v,phi):
    v_y=v*np.sin(phi*math.pi/180)
    v_x=v*np.cos(phi*math.pi/180)
    a=-9.81
    t=-2*v_y/a
    x_0=x_0+v_x*t
    return x_0

dt=0.02
analiticki=np.array(domet(0,0,10,60))
numericki=np.array(p1.range(dt))
T=np.arange(0,0.02)

while dt<=0.2:
    dt+=0.0005
    D=p1.range(dt)
    d=domet(0,0,10,60)
    analiticki=np.append(analiticki,d)
    numericki=np.append(numericki,D)
    T=np.append(T,dt)
   
error=100*abs(analiticki-numericki)/analiticki
plt.plot(T,error)
plt.xlabel("dt[s]")
plt.ylabel("Absolute relative error[%]")
plt.title("Absolute relative error for range of projectile")
plt.figtext(0.15,0.8,"(Err)=(100%)*abs(D(analitic)-D(numeric))/D(analitic)")
plt.show()
