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

x = np.arange(0,N*dx,dx)

k = 10e34 #set k = 1
omega = np.sqrt(k/m)

V = [(0.5*m*omega**2*i**2) for i in range(len(x))]  

def hermite(x):
    ''' Calculates Hermite polynomials by recursion formula '''
    H = []
    H0 = 1
    for i in range(len(x)):
        H1 = 2*i
        Hi = 2*x*H1-2(i-1)*H0
        H0 = H1
        H1 = Hi
        H.append(Hi)
    return Hi

def psi_theoretical(n, x):
    ''' Finds theoretical psi's '''
    psi = []
    for i in range(n):
        
        psi.append(psien)
    
    return psi

def plot_theoretical(n, psi, psi_theo, x):
    ''' Plots theoretical eigenfunctions psi '''
    plt_eigenfunctions(n,psi,x)
    H0 = 1
    for l in range(len(x)):
        H1 = 2*l
        Hi = 2*x*H1-2(i-1)*H0
        H0 = H1
        H1 = Hi
        
        psi_theo = [(1/np.sqrt(2**i*inp.math.factorial(i)))*((m*omega/(np.pi*h_bar))**(1/4))*np.exp(-(m*omega*l**2)/(2*h_bar))*hermite(np.sqrt((m*omega)*l/h_bar))]
        
        
    for i in range(n):
        
        plt.plot(x, psi_theo, label=(r"$\Tpsi_"+str(i)+"$"))
        plt.legend()
    #plt.xlim(0.0, 0.2*10e-9)
    plt.show()



E, psi = E_and_psi(x, V)

plot_eigenvalues(5, E, x)
plot_eigenfunctions(5, psi, x)
print_spread(5, E)

#Still need to plot the analytical solutions!