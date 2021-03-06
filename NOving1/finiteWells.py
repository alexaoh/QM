#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:37:58 2020

@author: ajo
"""
#More wells

import numpy as np
from plotEigenstuff import E_and_psi, plot_eigenvalues, plot_eigenfunctions, print_spread


h_bar = 1.0546e-34
m = 9.109e-31
N = 100
dx = 0.1e-10
L = N*dx

x = np.arange(0,N*dx,dx)

w = L/10

V0 = 10e-20

#LIGNER VELDIG PÅ PARTIKKEL I BOKS NÅR POTENSIALET ER LITE! HVORFOR DET? bURDE VÆRT NÅR POTENSIALET ER STORT. 

#side = [0]*((N-w)/2)
middle = [-V0 if 0<i<w else 0 for i in x]
#V = side + middle + side
V = middle

#Ser nesten lik ut som partikkel i boks? For veldig liten V_0
E, psi = E_and_psi(x, V)

plot_eigenvalues(5, E, x)
plot_eigenfunctions(5, psi, x)
print_spread(5, E)

#Still need to plot the analytical solutions!
