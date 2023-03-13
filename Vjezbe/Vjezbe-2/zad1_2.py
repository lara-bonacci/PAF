import numpy as np
import matplotlib.pyplot as plt

f=int(input("unesi iznos sile u N: "))
m=int(input("unesi iznos mase u kg: "))

a=f/m
v=0
x=0
t=np.arange(0,10.5,0.5)
put=np.array(x)
brzina=np.array(v)
akc=np.array([a]*len(t))


for N in range(20):

    v=v+a*0.5
    x=x+v*0.5
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

plt.show()



