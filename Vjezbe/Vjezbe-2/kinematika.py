import numpy as np
import matplotlib.pyplot as plt


def jednoliko_gibanje(f,m,dt): 
    a=f/m
    v=0
    x=0
    t=np.arange(0,10,dt)
    put=np.array(x)
    brzina=np.array(v)
    akc=np.array([a]*len(t))


    for N in range(int((10/dt)-1)):
        v=v+a*dt
        x=x+v*dt
        brzina=np.append(brzina,v)
        put=np.append(put,x)

    
   

    figure, axis = plt.subplots(3, 1, squeeze=False)
  
    axis[0,0].plot(t, put)
    axis[0,0].set_title("x-t graf")
    axis[0,0].set_ylabel("x[m]")
    axis[0,0].set_xlabel("t[s]")
  
    axis[1,0].plot(t, brzina)
    axis[1,0].set_title("v-t graf")
    axis[1,0].set_ylabel("v[m/s]")
    axis[1,0].set_xlabel("t[s]")
  
    axis[2,0].plot(t, akc)
    axis[2,0].set_title("a-t graf")
    axis[2,0].set_ylabel("a[m/s^(2)]")
    axis[2,0].set_xlabel("t[s]")

    #plt.show()


def kosi_hitac(v0,kut,dt):
    a_x=0
    a_y=-9.81
    v_x=v0*np.cos(kut)
    v_y=v0*np.sin(kut)
    x=0
    y=0
    t=np.arange(0,10,dt)
    x_os=np.array(x)
    y_os=np.array(y)



    for N in range(int((10/dt)-1)):
    
         v_x=v_x+a_x*dt
         x=x+v_x*dt
         v_y=v_y+a_y*dt
         y=y+v_y*dt
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
