import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

class Function1:

    def f(x):
        return x**3+x**2+x

    def i_f(x):
        return (x**4)/4 + (x**3)/3 + (x**2)/2
    
    def name():
        return "x**3+x**2+x"
    
class Function2:

    def f(x):
        return np.sin(x)

    def i_f(x):
        return -(np.cos(x))
    
    def name():
        return "sin(x)"

class Function3:

    def f(x):
        return 2*x**2 + 3
    
    def i_f(x):
        return (x**4)/2 + 3
    
    def name():
        return "2*x**2 + 3"


def graph(fja):
    N= np.arange(100,1000,50)

    U=[]
    L=[]
    IT=[]
    

    for n in N:
    
        u=calc.integration(fja.f,0,1,n)[0]
        l=calc.integration(fja.f,0,1,n)[1]
        it=calc.t_integration(fja.f,0,1,n)
        

        U.append(u)
        L.append(l)
        IT.append(it)

    
    plt.scatter(N,L,1,c="b",label="donja međa")
    plt.scatter(N,U,1,c="g",label="gornja međa")
    plt.scatter(N,IT,1,c="m",label="trapezna integracija")
    plt.title("Integracija funkcije {}".format(fja.name()))
    plt.xlabel("N koraka")
    plt.ylabel("integral od f(x)")
    plt.ylim([3.645,3.685])
    plt.legend(fontsize=7)


    plt.show()

graph(Function3)


