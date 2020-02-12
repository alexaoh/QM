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

omega = 100000

V = [(0.5*m*omega**2*i**2) for i in range(len(x))]

print(V)

E, psi = E_and_psi(x, V)

plot_eigenvalues(5, E, x)
plot_eigenfunctions(5, psi, x)
print_spread(5, E)

#Still need to plot the analytical solutions!