import numpy as np
import math
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,phi,mass,density,area,friction):
        self.v0=v0
        self.phi=phi
        self.vx=v0*np.cos(phi*math.pi/180)
        self.vy=v0*np.sin(phi*math.pi/180)
        self.mass=mass
        self.ro=density
        self.a=area
        self.c=friction
        self.ax=-np.sign(self.vx)*(self.ro*self.c*self.a/2)*self.vx**2
        self.ay=-9.81-np.sign(self.vy)*(self.ro*self.c*self.a/2)*self.vy**2
        self.x=0
        self.y=0

    def reset(self):
        self.vx=self.v0*np.cos(self.phi*math.pi/180)
        self.vy=self.v0*np.sin(self.phi*math.pi/180)
        self.ax=-np.sign(self.vx)*(self.ro*self.c*self.a/2)*self.vx**2
        self.ay=-9.81-np.sign(self.vy)*(self.ro*self.c*self.a/2)*self.vy**2
        self.x=0
        self.y=0

    def plot_euler(self,dt,color="b"):
        self.reset()
        y=[]
        x=[]
        
        while self.y>=0:
            x.append(self.x)
            y.append(self.y)
            self.ax=-np.sign(self.vx)*(self.ro*self.c*self.a/2)*self.vx**2
            self.ay=-9.81-np.sign(self.vy)*(self.ro*self.c*self.a/2)*self.vy**2
            self.vx+=self.ax*dt
            self.vy+=self.ay*dt
            self.x+=self.vx*dt
            self.y+=self.vy*dt
            
        plt.plot(x,y,color,label="dt={},Euler".format(dt))
        
    def plot_rungekutta(self,dt,color="r"):
        self.reset()
        y=[]
        x=[]
        
        
        while self.y>=0:
            x.append(self.x)
            y.append(self.y)
            k1vx=-np.sign(self.vx)*(self.ro*self.c*self.a/2)*self.vx**2*dt
            k1x=self.vx*dt 
            k2vx=-np.sign(self.vx+k1vx/2)*(self.ro*self.c*self.a/2)*(self.vx+k1vx/2)**2*dt
            k2x=(self.vx+k1vx/2)*dt
            k3vx=-np.sign(self.vx+k2vx/2)*(self.ro*self.c*self.a/2)*(self.vx+k2vx/2)**2*dt
            k3x=(self.vx+k2vx/2)*dt
            k4vx=-np.sign(self.vx+k3vx/2)*(self.ro*self.c*self.a/2)*(self.vx+k3vx/2)**2*dt
            k4x=(self.vx+k3vx/2)*dt
            self.vx+=(k1vx+2*k2vx+2*k3vx+k4vx)/6
            self.x+=(k1x+2*k2x+2*k3x+k4x)/6

            k1vy=(-9.81-np.sign(self.vy)*(self.ro*self.c*self.a/2)*self.vy**2)*dt
            k1y=self.vy*dt 
            k2vy=(-9.81-np.sign(self.vy+k1vy/2)*(self.ro*self.c*self.a/2)*(self.vy+k1vy/2)**2)*dt
            k2y=(self.vy+k1vy/2)*dt
            k3vy=(-9.81-np.sign(self.vy+k2vy/2)*(self.ro*self.c*self.a/2)*(self.vy+k2vy/2)**2)*dt
            k3y=(self.vy+k2vy/2)*dt
            k4vy=(-9.81-np.sign(self.vy+k3vy/2)*(self.ro*self.c*self.a/2)*(self.vy+k3vy/2)**2)*dt
            k4y=(self.vy+k3vy/2)*dt
            self.vy+=(k1vy+2*k2vy+2*k3vy+k4vy)/6
            self.y+=(k1y+2*k2y+2*k3y+k4y)/6



        plt.plot(x,y,color,label="dt={},Runge-Kutta".format(dt))
    

            

