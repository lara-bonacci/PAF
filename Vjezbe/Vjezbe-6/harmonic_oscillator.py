import numpy as np
import math 
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self,mass,k,x0,v0):
        self.m=mass
        self.k=k
        self.x=x0
        self.x00=x0
        self.v00=v0
        self.v=v0
        self.a=-self.k/self.m * self.x
        self.a00=-self.k/self.m * self.x00
        self.t=0
        
      
    
    def reset(self):
        
        self.x=self.x00
        self.v=self.v00
        self.t=0
        self.a=self.a00
        

    def amplitude(self,dt):
        self.reset()
        while self.v>=0:
            self.a=-self.k/self.m * self.x
            self.v=self.v + self.a*dt
            self.x=self.x+self.v*dt
        A=abs(self.x)
        return A
    
    def __move(self,dt):
        
        self.a=-self.k/self.m * self.x
        self.v+=self.a*dt
        self.x+=self.v*dt
        self.t+=dt

        
        return self.a,self.v,self.x,self.t
    
    def oscillate(self,t,dt):
        self.reset()
        T=[]
        acc=[]
        V=[]
        X=[]

        while self.t<=t:
            T.append(self.t)
            acc.append(self.a)
            V.append(self.v)
            X.append(self.x)
            self.__move(dt)

        return acc,V,X,T

        
    
    def plot_trajectory(self,t,dt,color="b",size=1):
      
        figure, axis = plt.subplots(3, 1, squeeze=False)
  
        axis[0,0].scatter(self.oscillate(t,dt)[3], self.oscillate(t,dt)[2],s=size,c=color,label="dt={}".format(dt))
        axis[0,0].set_title("x-t graf")
        axis[0,0].set_ylabel("x[m]")
        axis[0,0].set_xlabel("t[s]")
  
        axis[1,0].scatter(self.oscillate(t,dt)[3], self.oscillate(t,dt)[1],s=size,c=color,label="dt={}".format(dt))
        axis[1,0].set_title("v-t graf")
        axis[1,0].set_ylabel("v[m/s]")
        axis[1,0].set_xlabel("t[s]")
  
        axis[2,0].scatter(self.oscillate(t,dt)[3], self.oscillate(t,dt)[0],s=size,c=color,label="dt={}".format(dt))
        axis[2,0].set_title("a-t graf")
        axis[2,0].set_ylabel("a[m/s^(2)]")
        axis[2,0].set_xlabel("t[s]")

        plt.show()
    
        

    def time_period(self,dt):
        self.reset()
        self.__move(dt)
        
        while self.x>=-self.x:
            self.__move(dt)
            

        return self.t*4



    



        

