#this is max i'm a bum at code
#i'm kinda bad at coding so imma just pseudo code this based on the example\


#import math, plotting, optimization, and material libraries 


#fatigue_equation
# defines the equation for fatigue based on the material properties and strain


#function: calculate_strains_stresses
#input: loads, material_properties, geometry
#   loop over the segements of the structure grabbing from each part:
#   axial_stations = len(x_array)
#   for i in tqdm(range(0, axial_stations)): (going through all the parts of the structure)
#      material_properties, like yield strength 
#      thermal stresses, calculating based on temperature changes
#      Pressure Stresses, stress from internal and bulk pressures
#    combine these stresses(thermal and pressure) to get the total strains
#    use the von mises stress criterion(sick name) to see if it yields
#    use the coffin manson relation and the "custom fatigue equation" to calcluate cycles to failure
#    return the total strains, stresses, and cycles to failure
#    append all those results to arrays for analysis

# 1D Analysis 

import numpy as np
import matplotlib.pyplot as plt

    #Initializing variables 

L = 6.75 # Length of raceway in m 
A = 0.96 # Cross sectional area in m^2
E = 300e9 # Young's modulus in Pa (carbon fiber)
g = 9.81 # Gravitational acceleration in m/s^2
rho = 1600 # Density in kg/m^3 (carbon fiber)
p = 1.225 # Sea level standard air density (kg/m^3)
v = 343 # Mach 1 speed in m/s
C = 1.28 # drag coefficient for flate plate with normal vector parallel to drag vector
I = 2.08e-12 # Moment of inertia of carbon fiber beam 

# Forces in vertical direction (y)
f_cryo_normal = 2068576.14815 # Force from cryogenic load per unit length at 300 psi normal to the raceway cover (+y direction)
f_gravity = rho * A * g # Force from gravity per unit length in the -x direction (rho * A * g)
f_drag = 1/2 * p * (v ** 2) * C * A # Force from drag per unit length in the -x direction (length = 1 m)
f_thrust = 7500000 # force from thrust per unit length in the +x direction (length = 1 m)

f_horiz = f_thrust - f_drag - f_gravity # Net force in the +x direction 
f_vert = f_cryo_normal # Force from cryogenic load in the +y direction

#FEM Discretization 
n_nodes = 1000 # Number of nodes for FEA
n_elements = n_nodes - 1 # Number of elements for FEA]
dx = L / n_elements # Partial length 
x = np.linspace(0, L, n_nodes) # Node positions

# Global stiffness matrix + Force vector (horizontal = along x axis)
K_stretch = np.zeros((n_nodes, n_nodes))  # Assigning values of zero in a 1D Numpy array to the matrix to be updated later
f_stretch = np.zeros(n_nodes)  # Assigning values of zero in a 1D Numpy array to the force vector to be updated later

for i in range(n_elements):
    # Compute the element stiffness matrix for a 1D bar (2 nodes per element)
    ke = (E * A / dx) * np.array([[1, -1], 
                                  [-1, 1]])
    
    # Compute the equivalent nodal force vector for a constant distributed axial load
    fe = (f_horiz * dx / 2) * np.array([1, 1])  # Load is equally distributed to both nodes
    # Note that N/m * m = N, so this gives an actual force vector (not just a load per unit length)

    # Add the element stiffness matrix to the appropriate 2x2 block in the global stiffness matrix
    K_stretch[i:i+2, i:i+2] += ke

    # Add the element force vector to the corresponding entries in the global force vector
    f_stretch[i:i+2] += fe

# Apply axial boundary conditions: fixed at node 0
u_axial = np.zeros(n_nodes)
free_axial = list(range(1, n_nodes))
K_axial_red = K_stretch[np.ix_(free_axial, free_axial)]
F_axial_red = f_stretch[free_axial]
u_axial[free_axial] = np.linalg.solve(K_axial_red, F_axial_red)

# Shear Force, Moment, and Max Shear Stress ===
# Step 1: Define the constant distributed force array
f_vals = np.full_like(x, f_vert)

# Step 2: Manual cumulative trapezoidal integration (shear)
V = np.cumsum((f_vals[1:] + f_vals[:-1]) * np.diff(x) / 2)
V = np.insert(-V, 0, 0)  # Prepend 0 and negate for correct direction

# Step 3: Manual cumulative trapezoidal integration (moment)
M = np.cumsum((V[1:] + V[:-1]) * np.diff(x) / 2)
M = np.insert(M, 0, 0)

# Shear stress τ = VQ / (Ib)
h = 0.96  # height of rectangular cross-section in m
Q = (h/2) * (A/2)
tau_max = V * Q / (I * h)

# === 2. Vertical FEM (Euler-Bernoulli Beam) ===
K_bending = np.zeros((2*n_nodes, 2*n_nodes))
F_bending = np.zeros(2*n_nodes)

ke_b = (E * I / dx**3) * np.array([
    [12, -6*dx, -12, -6*dx],
    [-6*dx, 4*dx**2, 6*dx, 2*dx**2],
    [-12, 6*dx, 12, 6*dx],
    [-6*dx, 2*dx**2, 6*dx, 4*dx**2]
])

for i in range(n_elements):
    idx = [2*i, 2*i+1, 2*i+2, 2*i+3]
    fe_b = (f_vert * dx / 2) * np.array([1, dx/6, 1, -dx/6])   #fe is the element force vector 
    K_bending[np.ix_(idx, idx)] += ke_b
    F_bending[idx] += fe_b

# Apply vertical boundary conditions: fixed at node 0 (y and slope)
u_bending = np.zeros(2*n_nodes)
free_bending = list(range(2, 2*n_nodes))
K_bending_red = K_bending[np.ix_(free_bending, free_bending)]
F_bending_red = F_bending[free_bending]
u_bending[free_bending] = np.linalg.solve(K_bending_red, F_bending_red)

y_vertical = u_bending[::2]

# Use beam bending formula

# 1. Horizontal Displacement Plot (x-axcis)
plt.figure(figsize=(8, 5))
plt.plot(x, u_axial, '-o', linewidth=2, label='Horizontal displacement u(x)')
plt.xlabel('Position along bar (m)')
plt.ylabel('Displacement (m)')
plt.title('Horizontal Displacement of Raceway Cover')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Vertical Displacement Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_vertical, '-s', linewidth=2, label='Vertical displacement y(x)', color='orange')
plt.xlabel('Position along bar (m)')
plt.ylabel('Displacement (m)')
plt.title('Vertical Displacement of Raceway Cover')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 3. Combined Plot
plt.figure(figsize=(8, 5))
plt.plot(x, u_axial, '-o', linewidth=2, label='Horizontal u(x)')
plt.plot(x, y_vertical, '-s', linewidth=2, label='Vertical y(x)', color='orange')
plt.xlabel('Position along bar (m)')
plt.ylabel('Displacement (m)')
plt.title('Horizontal vs Vertical Displacement')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



