import em_polje as em
import matplotlib.pyplot as plt

e=em.ParticleEM(-1,1,1,1,1,1,1,5,0,0,10)
p=em.ParticleEM(1,1,1,1,1,1,1,5,0,0,10)


e.plot(0.001)
p.plot(0.001,color="r")




