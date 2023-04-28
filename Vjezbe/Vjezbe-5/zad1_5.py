import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

class Function1:
        
    def f(x):
        return x**3+x**2+x

    def d_f(x):
        return 3*x**2+2*x
    
    def name():
        return "x**3+x**2+x"

class Function2:
    def f(x):
        return np.sin(x)
    
    def d_f(x):
        return np.cos(x)

    def name():
        return "sin(x)"


def graph(fja):
    X= np.arange(-5,5,0.0005)
    a=[fja.d_f(x) for x in X]

    dx=0.01

    for color,color3 in zip(["c--","g--","m--"],["b--","y--","k--"]):
        n=calc.derivation(fja.f,-5,5,dx)[1]
        n3=calc.derivation(fja.f,-5,5,dx,calc.threestep_point_derivation)[1]
        plt.plot(X,n3,color3,linewidth=0.5,label="three-point derivacija s korakom {}".format(dx))
        plt.plot(X,n,color,linewidth=0.5,label="two-point derivacija s korakom {}".format(dx))
        dx=dx*10
    
   
    plt.plot(X,a,"r",label="analitička derivacija")
    plt.title("Derivacija funkcije {}".format(fja.name()))
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.legend(fontsize=7)

    plt.show()

graph(Function1)
graph(Function2)



