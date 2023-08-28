#!/usr/bin/env python
# coding: utf-8

# # 17 Oct 23 - Normal Modes

# ##  Three Coupled Oscillators
# 
# Consider the setup below consisting of three masses connected by springs to each other. We intend to find the normal modes of the system by denoting each mass's displacement ($x_1$, $x_2$, and $x_3$).
# 
# <img src="https://raw.githubusercontent.com/valentine-alia/phy415fall23/main/content/assets/3_coupled_osc.png" alt="3 coupled SHOs" width=800px/>
# 
# ### Finding the Normal Mode Frequencies
# 
# **&#9989; Do this** 
# 
# This is not magic as we will see, it follows from our choices of solution. Here's the steps and what you might notice about them:
# 
# 1. Guess what the normal modes might look like? Write your guesses down; how should the masses move? (It's ok if you are not sure about all of them, try to determine one of them)
# 2. Write down the energy for the whole system, $T$ and $U$ (We have done this before, but not for this many particles)
# 3. Use the Euler-Lagrange Equation to find the equations of motion for $x_1$, $x_2$, and $x_3$. (We have done this lots, so make sure it feels solid)
# 4. Reformulate the equations of motion as a matrix equation $\ddot{\mathbf{x}} = \mathbf{A} \mathbf{x}$. What is $\mathbf{A}$? (We have done this, but only quickly, so take your time)
# 5. Consider solutions of the form $Ce^{i{\omega}t}$, plug that into $x_1$, $x_2$, and $x_3$ to show you get $\mathbf{A}\mathbf{x} = -\omega^2 \mathbf{x}$. (We have not done this, we just assumed it works! It's ok if this is annoying, we only have to show it once.)
# 6. Find the normal mode frequencies by taking the determinant of $\mathbf{A} - \mathbf{I}\lambda$. Note that this produces the following definition: $\lambda = -\omega^2$ 
# 
# 

# ### Finding the Normal Modes Amplitudes
# 
# Ok, now we need to find the normal mode amplitudes. That is we assumed sinusoidal oscillations, but at what amplitudes? We will show how to do this with one frequency ($\omega_1$), and then break up the work of the the other two. These frequencies are:
# 
# $$\omega_A = 2\dfrac{k}{m}; \qquad \omega_B = \left(2-\sqrt{2}\right)\dfrac{k}{m}; \qquad \omega_C = \left(2+\sqrt{2}\right)\dfrac{k}{m}\qquad$$
# 
# **&#9989; Do this** 
# 
# After we do the first one, pick another frequencies and repeat. Answer the follow questions:
# 
# 1. What does this motion physically look like? What are the masses doing?
# 2. How does the frequency of oscillation make sense? Why is it higher or lower than $\omega_A$?
# 
# The two cells below have some code that shows how you could've used python to help you when solving this problem:

# In[22]:


import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy import Matrix # get symbolic matrix methods
init_printing(use_unicode=True) # make math display good

A = np.array([[-2, 1, 0], [1, -2, 1], [0, 1, -2]]) ## numpy matrix
A_sympy = Matrix(M) ## Take numpy matrix and make it a sympy one

eigenvals, eigenvects = np.linalg.eig(A) # numpy numerical methods
print("numpy eigenvals:",eigenvals)
print("numpy eigenvects:",eigenvects)
print("sympy eigenvals:")
A_sympy.eigenvals() # sympy symbolic methods WARNING: slow for big matrices


# In[21]:


print("sympy eigenvects:")
A_sympy.eigenvects()


# ## Extending your work
# 
# Given what we have done thus far, you can see that we could easily construct the matrix for a $N$ dimensional chain of 1D oscillators. So let's do that.
# 
# **&#9989; Do this** 
# 
# Repeat this analysis for a set of $N$ oscillators. Your code should be able to:
# 
# 1. Take a value of $N$ and construct the right matrix representation
# 2. Find the eigenvalues and eigenvectors for this matrix.
# 3. (BONUS) plots the modes automatically
# 4. (CHALLENGE) time the execution of the analysis
# 
# Be careful not to pick too large of an $N$ value to work with because you could melt your CPU easily. Make sure your code can do something like $N=10$. If you get the timing working, plot time vs number of objects to see how the problem scales with more oscillators.
# 

# In[ ]:


## Your code here


# ## Even further
# 
# These models can be used with lattices (solid objects). Draw a sketch of 4 oscillators in a plane connected together in a square shape. Write down the energy equations for this system (assume the springs do not move laterally much). What do the EOMs look like?

# ### Notes
# 
# * [Partial Solution to Activity](https://github.com/dannycab/phy415msu/blob/main/MMIPbook/assets/pdfs/notes/Notes_2_Three_Coupled_Oscillators.pdf)
# 
