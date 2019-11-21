import numpy as np
import matplotlib.pyplot as plt

print(np.sin(np.pi))



def dphi_r(r, dr, b, G, M,c):
    '''
    Function evaluates dphi as a function of r and dr
    inputs: r, dr
    outputs: dphi
    '''
    dphi = (np.sqrt(1/(((r**4)/(b**2)) - (r**2)*(1-2*G*M/(r*c**2)))))*dr
    
    return dphi


def dr_dphi(r, dphi, b, G, M ,c):
    '''
    Function allows for numerical integration by finding the change in r.
    inputs: r, dphi (change in phi, the step), b, G (gravitational constant),
    M (mass of black hole), c (speed of light)
    outputs: the change in the radius
    '''
    dr = (np.sqrt(np.absolute((r**4)/(b**2) - (r**2)*(1-(2*G*M)/(r*(c**2))))))*dphi
    
    return dr



# Create a list that will be filled with radius values
radii = []
# Create a list that will be filled with phi values
phi_values = []

# set dr
dr = 0.1

# Set phi initial
phi = 0

r = 0.0001

# Set b
b = 10**50

dphi = 0.1

# This for loop performs numerical integration on dr = (expression)dphi
for phi in np.arange(0,4*np.pi, dphi):
    
    # Send to function to update dr
    dr = dr_dphi(r, dphi, b, G=6.67*10**(-11), M=10**40, c=3*10**8)
    
    # add dr to raduis
    r += dr
    
    # Append to list for plotting 
    radii.append(r)
    phi_values.append(phi.item())
    

# for loop numerical integration of dphi = (expression)dr
#for r in np.arange(1,10,dr):
#    # Calculate the change in phi 
#    dphi = dphi_r(r.item(), dr, b, G=1, M=1, c=1)
#    
#    # Update phi value
#    phi += dphi
#    
#    # add phi and r value to phi and r lists
#    phi_values.append(phi)
#    radii.append(r)
    
print(phi_values)
print(radii)
#

plt.polar(phi_values, radii)
plt.show()
    
    