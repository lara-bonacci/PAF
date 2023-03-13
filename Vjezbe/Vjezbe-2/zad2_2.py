import numpy as np
import matplotlib.pyplot as plt

v0=int(input("unesi iznos početne brzine u m/s: "))
kut=int(input("unesi iznos kuta otklona u stupnjevima: "))

a_x=0
a_y=-9.81
v_x=v0*np.cos(kut)
v_y=v0*np.sin(kut)
x=0
y=0
t=np.arange(0,10.5,0.5)
x_os=np.array(x)
y_os=np.array(y)



for N in range(20):

    v_x=v_x+a_x*0.5
    x=x+v_x*0.5
    v_y=v_y+a_y*0.5
    y=y+v_y*0.5
    x_os=np.append(x_os,x)
    y_os=np.append(y_os,y)
    
   

figure, axis = plt.subplots(3, 1, squeeze=False)
  
axis[0,0].plot(x_os, y_os)
axis[0,0].set_title("x-y graf")
axis[0,0].set_ylabel("y[m]")
axis[0,0].set_xlabel("x[m]")
  
axis[1,0].plot(t, x_os)
axis[1,0].set_title("x-t graf")
axis[1,0].set_ylabel("x[m]")
axis[1,0].set_xlabel("t[s]")
  
axis[2,0].plot(t, y_os)
axis[2,0].set_title("y-t graf")
axis[2,0].set_ylabel("y[m]")
axis[2,0].set_xlabel("t[s]")

plt.show()