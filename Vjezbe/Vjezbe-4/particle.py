import matplotlib.pyplot as plt
import math
import numpy as np

class Particle:
    def __init__(self,x_0,y_0,v_0,phi):
        self.x_00=x_0
        self.x_0=x_0
        self.y_0=y_0
        self.y_00=y_0
        self.v_0=v_0
        self.phi=phi
        self.v_x=self.v_0*np.cos(self.phi*math.pi/180)
        self.v_y=self.v_0*np.sin(self.phi*math.pi/180)
        self.v_x0=self.v_0*np.cos(self.phi*math.pi/180)
        self.v_y0=self.v_0*np.sin(self.phi*math.pi/180)
        self.x_axis=np.array(self.x_00)
        self.y_axis=np.array(self.y_00)
       

    def reset(self):
        
        self.x_0=self.x_00
        self.y_0=self.y_00
        self.v_y=self.v_y0
        self.v_x=self.v_x0

    def __move(self,dt):
        
        a_x=0
        a_y=-9.81
        self.v_x=self.v_x+a_x*dt
        self.x_0=self.x_0+self.v_x*dt
        self.v_y=self.v_y+a_y*dt
        self.y_0=self.y_0+self.v_y*dt
        
        return self.x_0, self.y_0
    
    
    def range(self,dt):
        self.reset()
        while self.y_0>=0:
            self.__move(dt)
        
        return self.x_0
    
    def plot_trajectory(self,dt):
        self.reset()
        while self.y_0>=0:
        
            self.__move(dt)
            self.x_axis=np.append(self.x_axis,self.x_0)
            self.y_axis=np.append(self.y_axis,self.y_0)

        plt.plot(self.x_axis, self.y_axis)
        plt.title("x-y graf")
        plt.ylabel("y[m]")
        plt.xlabel("x[m]")
        plt.show()



       


