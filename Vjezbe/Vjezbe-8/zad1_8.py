import em_polje as em
import matplotlib.pyplot as plt

e=em.ParticleEM(-1,1, 0.1,0.1,0.1, 0,0,0, 0,0,1)
p=em.ParticleEM(1,1, 0.1,0.1,0.1, 0,0,0, 0,0,1)

dt=0.005
steps=5000

fig = plt.figure()
ax = plt.axes(projection ='3d')
r = e.euler(dt, steps)
ax.plot3D(r[0], r[1], r[2],"r")
r = p.euler(dt, steps)
ax.plot3D(r[0], r[1], r[2],"b")
ax.set_title('Nabijena čestica u EM polju')
plt.show()




