#!/usr/bin/env python
# coding: utf-8

# # 08 Sept 22 - Activity: Large Angle Pendulum
# 
# Up to now, most of your work with models in physics are those you can solve analytically in terms of known functions. Think about solving differential equations that produce polynomials or sines and cosines. 
# 
# But what happens when the solution to the problem is not obviously tractable in an analytical form. Rather, how can we investigate systems that are new to us?
# 
# This activity uses the Large Angle Pendulum. You probably have seen something like this before and maybe even worked with it. Below is a figure that describes the situation. Notice a lot of the geometry work has been done for you with this figure.
# 
# <img src="https://aapt.scitation.org/na101/home/literatum/publisher/aip/journals/content/ajp/2006/ajp.2006.74.issue-10/1.2215616/production/images/large/1.2215616.figures.f1.jpeg" alt="Large Angle Pendulum" width="600"/>
# 
# In this activity you will:
# 
# - Remind yourself how to interpret a phase portrait (phase space plot) using the SHO model
# - Explain what you see in the phase space figure for the SHO
# - Develop the ODE for the large angle pendulum
# - Show how we can recover the SHO using mathematics and graphs
# - Use an existing program to work with a new system
# - Explain the insights developed from a phase space plot of the Large Angle Pendulum
# - (if time) Plot a trajectories in the phase space
# - (if time) Add damping to the model

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ## Reminders about the SHO
# 
# To get this started, let's remind ourselves of the phase portrait of the SHO. Recall that we separated the second order ODE into two first order ODEs, one for $x$ and one for $v_x$,
# 
# $$\dot{x} = v_x$$
# $$\dot{v}_x=-\omega^2x$$
# 
# We then map out the phase space with the following conceptual interpretation:
# 
# - Phase space is a space in which all possible states of the system can be shown
#     - a state is a collection of conditions of the state (it's known position and velocity in our case)
# - Each state is a unique point in phase space
#     - Think about ordered Cartesian pairs, there's a pair of numbers for every point in a 2D space
# - Remember that knowing $x_0$ and $v_{x,0}$ means we can know $x(t)$ for all time (for that one trajectory/particular solution) given a linear ODE
# 
# We map the differential equation to the following conceptual interpretation: **How the state changes depends on location in phase space.** We can understand this as the time derivative for $x$ and $v_x$ change throughout the space.
# 
# For our 2D SHO case we are saying that how $x$ and $v_x$ change is proportional to the position in space:
# 
# $$\langle \dot{x}, \dot{v}_x \rangle = \langle v_x, -\omega^2 x\rangle$$
# 
# The process is:
# 
# 1. Determine the location(s) of interest (i.e., $x$, $v_x$)
# 2. Compute the change in those quantities at the location (i.e., calculate $\dot{x}$ and $\dot{v}_x$ using our prescribed 1st order ODEs above)
# 3. At a given point ($x_0$, $v_{x,0}$), create an arrow the indicates the direction and magnitude of the changes to $x$ and $v_x$ at that location.
#     - That arrow represents the local flow of the system at that point
# 4. Repeat for all points of interest
# 5. Plot arrows to demonstrate flow of the solutions in phase space

# ## Phase Portrait of the Simple Harmonic Oscillator
# 
# Below, we have written code that makes a phase portrait from the simple harmonic oscillator. It's written in terms of three functions that serve three purposes that you might want to modify in your own work:
# 
# * ``SHOPhasePortrait`` is a function that simply returns the relationship between the locations in phase space and how the phase variables change at that location. 
# * ``ComputeSHOPhase`` is a function that uses that relationship and computes the values of the changes at every location. It returns two arrays, which contain all those values.
# * ``SHOTrajectory`` is a function that takes a pair of points in space and computes the trajectory in phase space
# 
# By separating these ideas, we are illustrating the process for computing these phase portraits:
# - Translate the $N$th order differential equation to $N$ 1st order (Done earlier in this case)
# - Put that into a code so you can compute the value of the changes at a location (``SHOPhasePotrait``)
# - Call that computation a bunch to compute it at every location you want (``ComputeSHOPhase``)
# - investigate specific trajectories in the space (``SHOTrajectory``)
# 
# We can then call these functions can plots the results.

# In[2]:


def SHOPhasePortrait(x, vx, omega):
    '''SHOPhasePortrait returns the value of
    the change in the phase variables at a given location
    in phase space for the SHO model'''
    
    xdot, vxdot = [vx, -1*omega**2*x] ## Specific to this problem
    
    return xdot, vxdot


# In[3]:


def ComputeSHOPhase(X, VX, omega):
    '''ComputeSHOPhase returns the changes in 
    the phase variables across a grid of locations
    that are specified'''
    
    ## Prep the arrays with zeros at the right size
    xdot, vxdot = np.zeros(X.shape), np.zeros(VX.shape)

    ## Set the limits of the loop based on how 
    ## many points in the arrays we have
    Xlim, Ylim = X.shape
    
    ## Calculate the changes at each location and add them to the arrays
    for i in range(Xlim):
        for j in range(Ylim):
            xloc = X[i, j]
            yloc = VX[i, j]
            xdot[i,j], vxdot[i,j] = SHOPhasePortrait(xloc, yloc, omega)
            
    return xdot, vxdot


# In[4]:


def SHOTrajectory(x0, vx0, omega, N=100):
    '''SHOTrajectory computes the phase space
    trjectory using the analytical forms of the
    solution. Note this sloppy analytical approach
    only works because the SHO is perfectly sinusoidal.'''
    
    ## Only work with one period
    T = 2*np.pi/omega
    t = np.arange(0,T,T/N)
    
    ## I derived this in general with Acos(wt+phi)
    ## It's not in general a good approach
    ## because you are not guaranteed analytical 
    ## closed form trajectories in phase space
    
    phi = np.arctan2(-1*vx0, omega*x0) ## arctan(-vxo/(omega*x0)) taken correctly for the quadrant
    A = x0/np.cos(phi)
    x_traj = A*np.cos(omega*t+phi)
    v_traj = -omega*A*np.sin(omega*t+phi)
    
    return x_traj, v_traj


# ### Putting the functions to use
# 
# With these two functions, all we are left to do is specify the size of the space and the grid points (that is where exactly we are computing the changes). We use [meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) to make those arrays a set of Cartesian coordinates and then send that to our functions.
# 
# We then plots the results.

# In[5]:


## Setting parameters and the phase space variables

omega = 1
x = np.linspace(-10.0, 10.0, 20)
vx = np.linspace(-10.0, 10.0, 20)

## Get back pairs of coordinates for every point in the space
X, VX = np.meshgrid(x, vx)

## Run our calculations
xdot, vxdot = ComputeSHOPhase(X, VX, omega)

x0 = 5
vx0 = 3
x_traj, v_traj = SHOTrajectory(x0, vx0, omega)

## Plot. plot. plot.
ax = plt.figure(figsize=(10,6))
Q = plt.quiver(X, VX, xdot, vxdot, color='k')

## Plot trajectory and the starting location
plt.plot(x_traj,v_traj)
plt.plot(x0, vx0, 'r*', markersize=10)

plt.xlabel('$x$')
plt.ylabel('$v_x$')
plt.grid()


# ### What can phase space help us do? 
# 
# **&#9989; Do this** 
# 
# Let's remember a few things about the SHO. 
# 
# 1. With your neighbors, list all the things you know about the SHO. Include anything we haven't discussed (e.g., the energetics of the problem).
# 2. Name which of those things you can see in the phase diagram. Which things are you sure you can see? What things don't seem to be able to be seen from the phase diagram? 
# 3. What do you remember about the energy of an SHO? Consider a harmonic oscillator in a known trajectory ($x(t) = A\cos(\omega t)$). Compute the total (conserved) energy of the oscillator as a function of time. 
#     - Explain how your expression for energy conservation can be seen in your phase diagram. 
#     - You might try to show analytically that the ellipse above is related to your energy conservation expression
# 
# What does this plots tell you about all potential solutions?

# ## The Large Angle Pendulum
# 
# The Large Angle Pendulum is the first of a number of nonlinear differential equations out there. This one is quite special in that the integral that solves for the period of this pendulum has a name! It's called and [Elliptical Integral of the First Kind](https://en.wikipedia.org/wiki/Elliptic_integral). Elliptical because of the nature of the kernel of the integral, which has an elliptic form (in our case, one over the square root of a quantity squared subtracted from one, yes, seriously, we have a name for that).
# 
# Here's the pendulum in all it's glory.
# 
# ![Pendulum Bob](../../assets/images/pendulum_bob.png)
# 
# The analytical solution for the period is given by:
# 
# $$T = 4\sqrt{\dfrac{L}{g}}\int_0^{\pi/2}\dfrac{d\theta}{\sqrt{1-k^2\sin^2(\theta)}}$$
# 
# To find the period, we have to use some form of computation, even it's the "well-known" [recurrence relationship](https://en.wikipedia.org/wiki/Elliptic_integral#Complete_elliptic_integral_of_the_first_kind) that was used for centuries to compute this integral **by hand**.
# 
# But let's try to gain insight from the phase space instead. We can [derive] the differential equation that describes the motion of the pendulum through an angle $\theta$ thusly:
# 
# $$\ddot{\theta} = -\dfrac{g}{L}\sin(\theta)$$
# 
# You have a second order differential equation for $\theta$. 

# ### Make a new phase portrait
# 
# **&#9989; Do this** 
# 
# With your partners,
# 
# 1. Take the 2nd order ODE and make it two 1st order ODEs (one for $\theta$ and one for $\omega=\dot{\theta}$). Make sure you agree on the analytics.
# 2. Add those expressions to the function ```LAPPhasePortrait```
# 3. The rest of the code runs the same as before (we've engaged in reproducible and adaptable work!), so make some phase portraits. 
#     - What do you notice? 
#     - What physics is new? 
#     - What physics is old? 
# 4. Play with parameters and build a story for what is going on with the motion.
# 

# In[6]:


def LAPPhasePortrait(x, vx, omega0 = 10):
    
    #################
    ## CHANGE THIS ##
    #################
    xdot, vxdot = [1, 1] ## Specific to the problem
    
    return xdot, vxdot

def ComputeLAPPhase(X, VX, omega0):
    
    xdot, vxdot = np.zeros(X.shape), np.zeros(VX.shape)

    Xlim, Ylim = X.shape
    
    for i in range(Xlim):
        for j in range(Ylim):
            xloc = X[i, j]
            yloc = VX[i, j]
            xdot[i,j], vxdot[i,j] = LAPPhasePortrait(xloc, yloc, omega0)
            
    return xdot, vxdot


# In[7]:


omega0 = 2
N = 40

x = np.linspace(-6.0, 6.0, N)
vx = np.linspace(-8.0, 8.0, N)

X, VX = np.meshgrid(x, vx)

xdot, vxdot = ComputeLAPPhase(X, VX, omega0)

ax = plt.figure(figsize=(10,6))
Q = plt.quiver(X, VX, xdot, vxdot, color='k')
plt.grid()

plt.xlabel('$x$')
plt.ylabel('$v_x$')


# In[ ]:




