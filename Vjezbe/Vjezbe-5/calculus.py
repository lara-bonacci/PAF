import numpy as np
import math

def twostep_point_derivation(f,x,dx):
    der2=(f(x+dx)-f(x))/dx
    return der2

def threestep_point_derivation(f,x,dx):
    der3=(f(x+dx)-f(x-dx))/2*dx
    return der3


def derivation(f,min,max,dx,method=twostep_point_derivation):
    range_=np.arange(min,max,0.0005)

    der_range=[method(f,x,dx) for x in range_]
        
    return range_, der_range

def integration(f,min,max,n):
    d=(max-min)/n
    upper=0
    lower=0
    for x in np.linspace(min,max-d,n):
        lower+=f(x)*d
    for x in np.linspace(min+d,max,n):
        upper+=f(x)*d

    return upper,lower

def t_integration(f,min,max,n):
    d=(max-min)/n
    suma=0
    for x in np.arange(min+d,max,d):
        suma+=f(x)
    integral=d*(suma+(f(min)+f(max))/2)
    return integral










