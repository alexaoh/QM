import numpy as np
from plotEigenstuff import E_and_psi, plot_eigenvalues, plot_eigenfunctions, print_spread
import matplotlib.pyplot as plt


h_bar = 1.0546e-34
m = 9.109e-31
N = 100
dx = 0.1e-10
L = N*dx
n = 5
e_charge = 1.602e-19
x = np.arange(0,N*dx,dx)

V = [0 for i in range(len(x))]

E, psi = E_and_psi(x, V)



def psi_theoretical(n, x):
    ''' Finds theoretical psi's '''
    psi = np.sqrt(2/L)*np.sin(n*np.pi*x/L)
    return psi

def E_theoretical(n):
    ''' Returns theoretical energy-values '''
    return (n**2*np.pi**2*h_bar**2)/(2*m*L**2)

def make_lists(n, x):
    ''' Makes lists out of each theoretical value '''
    psi_theo = np.zeros(len(x))
    E_theo = np.zeros(len(x))
    for i in range(len(x)):
        psi_theo[i] = psi_theoretical(n,i)
        E_theo[i] = E_theoretical(n) 
    return psi_theo, E_theo

def plot_theoretical_eigenfunctions(n, x):
    ''' Plots eigenfunctions psi '''        
    for i in range(n):
        psi_theo, E_theo = make_lists(n, x)
        plt.plot(x,psi_theo, label=(r"$\psi_"+str(i)+"$"))
        plt.legend()
    #plt.xlim(0.0, 0.2*10e-9)
    plt.xlabel('x (nm)')
    plt.ylabel('Eigenfunctions')
    plt.title(str(n)+' theoretical eigenfunctions')
    plt.show()
    

def plot_theoretical_eigenvalues(n, x):
    ''' Plots eigenvalues E '''
    for i in range(n):
        E_theo = E_theoretical(i)
        plt.plot(x, [E_theo/e_charge for l in range(len(x))], label=(r"$E_"+str(i)+"$"))
        plt.legend()
    plt.xlabel('x (nm)')
    plt.ylabel('Eigenvalues (eV)')
    plt.title(str(n)+' theoretical eigenvalues')
    plt.show()

psi_theo, E_theo = make_lists(n, x)

plot_eigenvalues(n, E, x)
plot_eigenfunctions(n, psi, x)
plot_theoretical_eigenvalues(n, x)
plot_theoretical_eigenfunctions(n, x)
print_spread(n, E)
print_spread(n, E_theo)

