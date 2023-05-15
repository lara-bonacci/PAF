import projectile as pro
import matplotlib.pyplot as plt

p1=pro.Projectile(15,30,1,1.2,0.0025,0.2)

p1.plot_euler(0.1)
p1.plot_euler(0.01,"m")
p1.plot_euler(0.001,"g")
p1.plot_rungekutta(0.01)
plt.title("x-y graph")
plt.xlabel("x[m]")
plt.ylabel("y[m]")
plt.legend()
plt.show()