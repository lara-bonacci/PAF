import numpy as np
import matplotlib.pyplot as plt

class ParticleEM:
    def __init__(self,q,m,vx,vy,vz,ex,ey,ez,bx,by,bz):
        self.v=np.array((vx,vy,vz),dtype=np.float64)
        self.e=np.array((ex,ey,ez),dtype=np.float64)
        self.b=np.array((bx,by,bz),dtype=np.float64)
        self.q=q
        self.m=m
        self.a=0.0
        #self.a=(q/m)*(self.e+np.cross(self.v,self.b))
        self.v0=np.array((vx,vy,vz),dtype=np.float64)
        self.e0=np.array((ex,ey,ez),dtype=np.float64)
        self.b0=np.array((bx,by,bz),dtype=np.float64)
        #self.a0=(self.q/self.m)*(self.e+np.cross(self.v,self.b))
        self.w=np.array((0.,0.,0.))

    def reset(self):
        self.v=self.v0
        self.e=self.e0
        self.b=self.b0
        self.a=0
        self.w=np.array((0.,0.,0.))
        

    def runge_kutta(self,dt,steps):
        self.reset()  

        x=[]
        y=[]
        z=[]

        for i in range(steps):
    
            x.append(self.w[0])
            y.append(self.w[1])
            z.append(self.w[2])
            
            k1v=(self.q/self.m)*(self.e+np.cross(self.v,self.b))*dt
            k1=self.v*dt 
            k2v=(self.q/self.m)*(self.e+np.cross(self.v+k1v/2,self.b))*dt
            k2=(self.v+k1v/2)*dt
            k3v=(self.q/self.m)*(self.e+np.cross(self.v+k2v/2,self.b))*dt
            k3=(self.v+k2v/2)*dt
            k4v=(self.q/self.m)*(self.e+np.cross(self.v+k3v/2,self.b))*dt
            k4=(self.v+k3v/2)*dt
            self.v+=(k1v+k2v*2+k3v*2+k4v)/6
            np.add(self.w,(k1+k2*2+k3*2+k4)/6,out=self.w,casting="unsafe")
            
       

        return x,y,z

    def euler(self,dt,steps):
        self.reset()  

        x=[]
        y=[]
        z=[]

        for i in range(steps):
    
            x.append(self.w[0])
            y.append(self.w[1])
            z.append(self.w[2])
            
            self.a=(self.q/self.m)*(self.e+np.cross(self.v,self.b))
            self.v+=self.a*dt
            self.w+=self.v*dt
            
            
        return x,y,z
        
        


