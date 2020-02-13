#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Wed Feb 12 11:30:36 2020

@author: ajo
'''

import numpy as np
from plotEigenstuff import E_and_psi, plot_eigenvalues, plot_eigenfunctions, print_spread


h_bar = 1.0546e-34
m = 9.109e-31
N = 100
dx = 0.1e-10
L = N*dx
n = 5
x = np.arange(0,N*dx,dx)

#k = 10e34 #set k = 1
#omega = np.sqrt(k/m)
omega = 1e-2

V = [(0.5*m*omega**2*i**2) for i in range(len(x))]  

def hermite(n, x):
    ''' Calculates Hermite polynomials by recursion formula '''
    H0 = 1
    H1 = 2*x
    for i in range(2,n):
        Hi = 2*x*H1-2*(i-1)*H0
        H0 = H1
        H1 = Hi
    return Hi

def psi_theoretical(n, x):
    ''' Finds theoretical psi's '''
    h_n = hermite(n,np.sqrt((m*omega)/h_bar)*x)
    psi = (1/np.sqrt(2**n*np.math.factorial(n)))*((m*omega/(np.pi*h_bar))**(1/4))*np.exp(-(m*omega*x**2)/(2*h_bar))*h_n
    return psi

def E_theoretical(n):
    ''' Returns theoretical energy-values '''
    return (n+(1/2))*h_bar*omega

def make_lists(n, x):
    ''' Makes lists out of each theoretical value '''
    psi_theo = np.zeros(len(x))
    E_theo = np.zeros(len(x))
    for i in range(len(x)):
        psi_theo[i] = psi_theoretical(n,i)
        E_theo[i] = E_theoretical(n) 
    return psi_theo, E_theo

E, psi = E_and_psi(x, V)
E_theo, psi_theo = make_lists(n, x)

plot_eigenvalues(n, E, x)
plot_eigenfunctions(n, psi, x)
plot_eigenvalues(n, E_theo, x)
plot_eigenfunctions(n, psi_theo, x)
print_spread(n, E)
print_spread(n, E_theo)
