import numpy as np
import matplotlib.pyplot as plt

class Body:
        def __init__(self,name,color,mass,initial_d,initial_velocity):
            self.m=mass
            self.n=name
            self.c=color
            self.d=initial_d
            self.v=initial_velocity
 


class System:
    def __init__(self,body1,body2):
        self.g=6.67408*10**(-11)
        self.c1=body1.c
        self.c2=body2.c
        self.n1=body1.n
        self.n2=body2.n
        self.m1=body1.m
        self.m2=body2.m
        self.d1=body1.d
        self.d2=body2.d
        self.v1=body1.v
        self.v2=body2.v
        
        
        
    def __step(self,dt):
        a1=-(self.g*self.m2*(self.d1-self.d2))/(abs(self.d1-self.d2))**3
        self.v1+=a1*dt
        self.d1+=self.v1*dt
        
        a2=-(self.g*self.m1*(self.d2-self.d1))/(abs(self.d2-self.d1))**3
        self.v2+=a2*dt
        self.d2+=self.v2*dt
     



    def simulate(self,dt,T=365.242):
     
        for t in np.arange(0,T,dt):

            self.__step(dt)
            
        
        figure, axes = plt.subplots()
        plt.scatter(0,self.d1,color=self.c1)
        plt.scatter(0,self.d2,color=self.c2)
        path2 = plt.Circle( (0, 0 ), self.d2, fill = False, color=self.c2)
        path1 = plt.Circle( (0, 0 ), self.d1, fill = False, color=self.c1)
        axes.set_aspect( 1 )
        axes.add_artist(path1)
        axes.add_artist(path2)
        if self.d2>self.d1:
             plt.xlim(-1.5*self.d2,1.5*self.d2)
             plt.ylim(-1.5*self.d2,1.5*self.d2)
        else:
             plt.xlim(-1.5*self.d1,1.5*self.d1)
             plt.ylim(-1.5*self.d1,1.5*self.d1)
             
        plt.title( '{}-{}'.format(self.n1,self.n2) )
        plt.show()
        
        
        