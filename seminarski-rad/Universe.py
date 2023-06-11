import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import moviepy
import ffmpeg

G=6.67408e-11
AU=1.5e11
dt=1*24*3600

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

class Planet:
    def __init__(self,name,size,color,mass,initial_position,initial_velocity):

        self.m=mass
        self.n=name
        self.s=size
        self.c=color
        self.d=np.array(initial_position)
        self.v=np.array(initial_velocity)
        self.path_x=[self.d[0]]
        self.path_y=[self.d[1]]
   


    def step(self,bodies,dt):

        a=0

        for b in bodies:
            if b!=self:
                d=self.d-b.d
                a+=-G*b.m*d/(d[0]**2+d[1]**2)**1.5   
        
        self.v+=dt*a
        self.d+=self.v*dt
        self.path_x.append(self.d[0])
        self.path_y.append(self.d[1])
        
        
       
    

    def plot(self,axes):
        self.path,=axes.plot(self.path_x,self.path_y,color="dimgray",linestyle=":",markersize=2)
        self.planet,=axes.plot(self.d[0],self.d[1],color=self.c,marker="o",markersize=self.s)
        self.text=axes.text(self.d[0],self.d[1],'{}'.format(self.n))
        
        
        

    def update(self,bodies,dt):
        self.step(bodies,dt)
        self.path.set_data(self.path_x,self.path_y)
        self.planet.set_data(self.d[0],self.d[1])
        self.text.set_position([self.d[0],self.d[1]])
        
        return [self.planet,self.path,self.text]


class Universe:
    def __init__(self,*bodies):
        self.figure=plt.figure()
        self.axes = plt.axes()

        self.bodies=bodies

        

    def step(self,dt):
        for b in self.bodies:
            b.step(self.bodies,dt)
        
    def update(self,frame):
  
        for b in self.bodies:

            b.update(self.bodies,dt)


    def simulate(self,T_inseconds):
        
        self.axes.set_xlim(-AU*2,AU*2)
        self.axes.set_ylim(-AU*2,AU*2)
 
        
        for b in self.bodies:
            b.plot(self.axes)
            
        
        ani = animation.FuncAnimation(fig=self.figure, func=self.update,frames=T_inseconds)
            
        
        ani.save('solarsystem.mp4', fps=30, writer=writer)

