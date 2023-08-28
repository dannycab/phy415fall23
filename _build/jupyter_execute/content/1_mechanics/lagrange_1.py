#!/usr/bin/env python
# coding: utf-8

# # 5 Sep 23 - Calculus of Varations and Lagrangian Dynamics

# The name of the game in calculus of variations is finding minimums,maximums, or stationary points of integrals that have the form:
# 
# 
# $$
# S = \int_{x_1}^{x_2} f[y(x),\dot{y}(x),x] dx
# $$
# 
# While you are trying to find the minimize $S$, what you end up finding is the **function** $y(x)$ that satisfies this minimization. It turns out that for $S$ to have extrema, the Euler-Lagrange equation (below) must be satisfied.
# 
# $$
# \frac{\partial f}{\partial y} - \frac{d}{dx}\left(\frac{\partial f}{\partial \dot{y}} \right) = 0
# $$
# 
# In practice, when approaching a varational problem, the typical worflow if something like this:
# 
# 1. Write your problem down in the form of an integral like $S$.
# 2. Use the Euler-Lagrange equation to get a differential equation for the unknown function $y$.
# 3. Solve the differential equation.
# 
# We can extend this framework for use in classical mechanics by defining the lagrangian of a system with independent, generalized coordinates $(q_1,\dot{q}_1... q_n,\dot{q}_n)$ as the kinetic energy minus potential energy of a system:
# 
# $$
# \mathcal{L(q_1,\dot{q}_1... q_n,\dot{q}_n)} = T(q_1,\dot{q}_1... q_n,\dot{q}_n) - V(q_1,\dot{q}_1... q_n,\dot{q}_n)
# $$
# 
# Then we write the action of the system as:
# 
# $$
# S = \int_{t_1}^{t_2} \mathcal{L(q_1,\dot{q}_1... q_n,\dot{q}_n)} dt
# $$
# 
# It turns out that the path a system takes between points $1$ and $2$ in the generalized coordinates is the path such that $S$ is stationary. This is called the principle of least action. This lets us leverage the  Euler-Lagrange equation for the generalized coordinates of our system $q_n$.
# 
# $$
# \frac{\partial \mathcal{L}}{\partial q_i} - \frac{d}{dx}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}_i} \right) = 0
# $$
# 
# This gives us $n$ equations of motion (EOM) for our system. Note how we didn't have to know anything about the forces acting on our system to arrive at equations of motion. 

# ## Activity
# 
# ### Simple Harmonic Oscillator (SHO)
# 
# **&#9989; Do this** 
# 
# 1. Starting with the 1d energy equations ($T$ and $V$) for a SHO; derive the equations of motion. Did you get the sign right?
# 
# ### Canonical Coupled Oscillators
# 
# Let's assume you have a chain of two mass connected by springs (all with the same $k$) as below.
# 
# <img src='https://www.entropy.energy/static/resources/coupled-oscillators/two-coupled-gliders-diagram.png' alt='Coupled Oscillator set up. Two oscillators connected by three springs in a horizontal line.' width=800px/>
# 
# **&#9989; Do this** 
# 
# 1. Write down the energy equations for this system (using $x_1$ and $x_2$ for coordinates)
# 2. Write the Lagrangian and derive the two equations of motion.
# 3. Do all the signs makes sense to you?
# 4. Could you have arrived at these equations in the newtonian framework?

# ### 2-Body Problem
# 
# Consider the 2 body problem of a star and an orbiting planet under the force of gravity. Assume the star is stationary. 
# 
# **&#9989; Do this** 
# 
# 1. Write down the energy equations for this system using polar coordinates.
# 2. Write the Lagrangian and derive 2 equations of motion for $r$ and $\phi$

# ## Adding Constraint Forces
# 
# The Lagrangian framework also excells at dealing with constrained motion, where it is usually not obvious what the constraint forces are. This is because you can write your generalized coordinates for your system in such a way that it contains the information
# 
# 
# 
# Consider a particle of mass $m$ constrained to move on the surface of a paraboloid $z =  r^2$ subject to a gravitational force downward, so that the paraboloid and gravity are aligned.
# 
# **&#9989; Do this** 
# 
# 
# 1. Using cylindrical coordinates (why?), write down the equation of constraint. Think about where the mass must be if it's stuck on a paraboloid.
# 2. Write the energy contributions in cylindrical coordinates. (This is where you put in the constraint!)
# 3. Form the Lagrangian and find the equations of motion (there are two!)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def parabaloid(x,y,alpha):
    # function of a paraboloid in Cartesian coordinates
    return alpha * (x**2 + y**2)

# points of the surface to plot
x = np.linspace(-2.8, 2.8, 50)
y = np.linspace(-2.8, 2.8, 50)
alpha = 1
# construct meshgrid for plotting
X, Y = np.meshgrid(x, y)
Z = parabaloid(X, Y,alpha)

# do plotting
fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
plt.title(r"Paraboloid ($\alpha = $" + str(alpha)+ ")")
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='binary', alpha=0.8) 
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-1 ,15)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()


# ### Roller Coaster
# 
# Consider 3 roller coaster cars of equal mass $m$ and positions $x_1,x_2,x_3$, constrained to move on a one dimensional "track" defined by $f(x) = x^4 -2x^2 + 1$. These cars are also constrained to stay a distance $d$ apart, since they are linked. We'll only worry about that distance $d$ in the direction for now (though a fun problem would be to try this problem with a true fixed distance!)

# In[2]:


x = np.arange(-1.8,1.8,0.01)
track = lambda x : x**4 - 2*x**2 + 1
y = track(x)
d = 0.1
x1_0 = -1.5
x2_0 = x1_0 - d
x3_0 = x1_0 - 2*d
plt.plot(x,y, label = "track")
plt.scatter(x1_0,track(x1_0),zorder = 2,label = r"$x_1$")
plt.scatter(x2_0,track(x2_0),zorder = 2,label = r"$x_2$")
plt.scatter(x3_0,track(x3_0),zorder = 2,label = r"$x_3$")
plt.legend()
plt.grid()
plt.show()


# **&#9989; Do this** 
# 
# 1. Write down the equation(s) of constraint. How many coordinates do you actually need?
# 2. Write the energies of the system using your generalized coordinates.
# 3. Form the Lagrangian and find the equation(s?) of motion (how many are there?)
# 4. Are the dynamics of this system different that the dynamics of a system of just one roller coaster car?
