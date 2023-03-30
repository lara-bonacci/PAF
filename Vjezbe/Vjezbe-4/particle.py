import matplotlib.pyplot as plt
import math
import numpy as np

class Particle:
    def __init__(self,x_0,y_0,v_0,phi):
        self.x_0=x_0
        self.y_0=y_0
        self.v_0=v_0
        self.phi=phi
        a_x=0
        a_y=-9.81
        v_x=self.v_0*np.cos(self.phi*math.pi/180)
        v_y=self.v_0*np.sin(self.phi*math.pi/180)
        x_axis=np.array(self.x_0)
        y_axis=np.array(self.y_0)

    def reset(self):
        
        self.x_0=0
        self.y_0=0
        self.v_0=0
        self.phi=0

    def __move(self,dt):
        
        v_x=v_x+a_x*dt
        self.x_0=self.x_0+v_x*dt
        v_y=v_y+a_y*dt
        self.y_0=self.y_0+v_y*dt
        x_axis=np.append(x_axis,self.x_0)
        y_axis=np.append(y_axis,self.y_0)

        return x_axis, y_axis
    
    
    def range(self,dt):
        a_x=0
        a_y=-9.81
        v_x=self.v_0*np.cos(self.phi*math.pi/180)
        v_y=self.v_0*np.sin(self.phi*math.pi/180)
        x_axis=np.array(self.x_0)
        y_axis=np.array(self.y_0)
        while self.y_0>=0:
            __move(self,dt)
        domet=x_axis[-1]
        return domet
    
    def plot_trajectory(self,dt):
        while self.y_0>=0:
            __move(self,dt)
        plt.plot(x_axis, y_axis)
        plt.set_title("x-y graf")
        plt.set_ylabel("y[m]")
        plt.set_xlabel("x[m]")
        plt.show()

       


