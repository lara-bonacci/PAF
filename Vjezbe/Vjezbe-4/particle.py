class Particle:
    def __init__(self,mass,x_0,v_0):
        self.mass=mass
        self.x_0=x_0
        self.v_0=v_0

    def printInfo(self):
        print("masa čestice=",self.mass)
        print("položaj čestice=",self.x_0)
        print("početna brzina čestice=",self.v_0)

    def moveToOrigin(self):
        self.x_0=0

    def accelerate(self,v):
        self.v_0=self.v_0+v

p1=Particle(10,10,20)
p1.printInfo()
p1.moveToOrigin()
p1.accelerate(5)
p1.printInfo()
