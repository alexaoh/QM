from scipy.linalg import eigh_tridiagonal
import numpy as np
import matplotlib.pyplot as plt

h_bar = 1.0546e-34
m = 9.109e-31
N = 100
dx = 0.1e-10
L = N*dx

x = np.arange(0,N*dx,dx)

def E_and_psi(x,V):
    ''' Calculates lists of E and psi '''
    d = np.asarray([h_bar**2/(m*dx**2)+v for v in V])
    e = np.asarray([-h_bar**2/(2*m*dx**2) for i in x[:len(x)-1]])
    E, psi = eigh_tridiagonal(d,e)
    return E,psi

def plot_eigenvalues(n, E, x):
    ''' Plots eigenvalues E '''
    plt.figure()
    for i in range(n):
        plt.plot(x, [E[i] for l in range(len(x))], label=(r"$E_"+str(i)+"$"))
        plt.legend()
    plt.xlabel('x (nm)')
    plt.ylabel('Eigenvalues')
    plt.title(str(n)+' eigenvalues')
    plt.show()


def plot_eigenfunctions(n, psi, x):
    ''' Plots eigenfunctions psi '''
    for i in range(n):
        plt.plot(x, psi[:, i], label=(r"$\psi_"+str(i)+"$"))
        plt.legend()
    plt.xlabel('x (nm)')
    plt.ylabel('Eigenfunctions')
    plt.title(str(n)+' eigenfunctions')
    plt.show()

def print_spread(n, E):
    ''' Prints spread between eigenvalues '''
    for i in range(1,n+1):
        ratio = round(E[i]/E[0],3)
        print("The ratio between eigenvalues", i, "and 0 is", ratio)

