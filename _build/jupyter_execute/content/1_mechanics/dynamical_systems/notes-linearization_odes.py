#!/usr/bin/env python
# coding: utf-8

# # 19 Sep 23 - Notes: Heading towards Chaos
# 
# One of the principal motivations for our work thus far has been to get to analyze systems that show suprising and complex behavior. In mechanics, you might have heard of those kinds of behviors as chaotic or exhibiting chaos. It turns out the chaos is a specific kind of behavior that we can find. To motivate us, let's remind ourselves of how cool nature can be.
# 
# [![](https://markdown-videos-api.jorgenkh.no/youtube/fDek6cYijxI?width=720&height=405)](https://inv.tux.pizza/watch?v=fDek6cYijxI)
# 

# ## Reminders of the Large Angle Pendulum
# 
# Last time we investigated the phase portrait of the large angle pendulum, we we could arrive at by re-writing the differential equation 
# 
# $$
# \ddot{\theta} = -\dfrac{g}{L}\sin(\theta)
# $$
# 
# as 2 first-order differential equations:
# 
# $$
# \dot{\theta} = \omega \hspace{0.5in}\text{and}\hspace{0.5in} \dot{\omega} = -\frac{g}{L}\sin(\theta)
# $$
# 
# By setting both of these equations equal to zero simultaneously, we also argued that this system has ([countably](https://faculty.math.illinois.edu/~kapovich/417-16/card.pdf)) infinite fixed points at $(n\pi, 0)$ for  $n\in \mathbb{Z}$ in $(\theta,\omega)$ phase space. 
# 
# ### Linearization and the Jacobian
# 
# Now we turn to the challenge of characterizing these fixed points with the linearization of the system (see the end of tuesday's activity for some more notes on this). Recall that we can do this by finding the eigenvalues of the Jacobian Matrix of the system at its fixed point. For the system $\dot{x} = f(x,y)$, $\dot{y} = g(x,y)$ the jacobian matrix looks like this:
# 
# $$
# A = \begin{bmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \\ \frac{\partial g}{\partial x} & \frac{\partial g}{\partial y}\end{bmatrix}_{(x^*,y^*)}
# $$
# 
# **&#9989; Try this** 
# 
# 
# Calculate the general Jacobian matrix $A$ for this system, then calculate what it is at the fixed point $(0,0)$.
# 
# We have the Jacobian at $(0,0)$ now but we still need to find its eigenvalues. Let's remind ourselves about eigenvalues and eigenvectors.

# ## Eigenvalues
# 
# Eigenvalues and the closely related Eigenvectors are indispensible in physics, math, and computational science. These ideas for the basis (pun somewhat intened) for countless problems, from the [energy eigenvalue equation](https://phys.libretexts.org/Bookshelves/Nuclear_and_Particle_Physics/Introduction_to_Applied_Nuclear_Physics_(Cappellaro)/02%3A_Introduction_to_Quantum_Mechanics/2.04%3A_Energy_Eigenvalue_Problem) that is the foundation of quantum mechanics, to the stability of complex nonlinear systems, to Normal Modes of oscillators. *Eigenproblems* show up all over in physics. 
# 
# A brief tangent: Once some scientists were using an eigenvalue driven algorithm called principal component analysis to study the genes of people that live in Europe. They found that these eigenvalues/vectors reproduced a map of Europe with surprising accuracy ([link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735096/)). So these tools are extremely, and often unreasonably powerful.
# 
# Eigenvalues are the $\lambda$ in the equation:
# 
# $$
# A\mathbf{v} = \lambda \mathbf{v}
# $$
# 
# Where $A$ is a linear operator of the vector space that $\mathbf{v}$ lives in. In finite-dimensional vector spaces, rhese linear operators are always matrices. There is a bit of physical intuition behind this equation: An eigenvector of $A$ is a vector that only gets stretched or squished by $\lambda$ when $A$ acts on $\mathbf{v}$. 
# 
# ### Video from 3Blue1Brown
# 
# Grant Sanderson makes a lot of great videos on mathematics and statistics. This one about eigenvalues and eigenvectors is particularly good.
# 
# [![](https://markdown-videos-api.jorgenkh.no/youtube/PFDu9oVAE-g?width=720&height=405)](https://inv.tux.pizza/watch?v=PFDu9oVAE-g)
# 
# 
# ### Finding Eigenvalues
# 
# To actually find the eigenvalues of a matrix, you solve the **characteristic polynomial** of the matrix, which you obtain by solving the equation:
# 
# $$
# |A - \lambda I | = 0 
# $$
# 
# Where the vertical bars means determinant.
# 
# To find Eigenvectors, simply plug in the values you found for $\lambda$ into the original eigenvalue equation $A\mathbf{v} = \lambda \mathbf{v}$, using $\mathbf{v} = \begin{bmatrix}x \\ y\end{bmatrix}$. You'll find some simple relationship between $x$ and $y$. Any scalar multiple of an eigenvector is also an eigenvector so we usually just choose the simplest one. Say if you found that $x = -y$. Then for a nice clean looking eigenvector you could choose $\begin{bmatrix} -1 \\ 1\end{bmatrix}$. 
# 
# **&#9989; Try this** 
# 
# Analytically, find the eigenvalues of the Jacobian matrix you calculated earlier. Use the below bullets to identify these eigenvalues with the type of the fixed point.
# 
# - $\mathrm{Re}(\lambda) > 0 $ for both eigenvalues: Repeller/Source (unstable)
# - $\mathrm{Re}(\lambda) < 0 $ for both eigenvalues: Attractor/Sink  (stable)
# - One eigenvalue positive, one negative: Saddle
# - Both eigenvalues pure imaginary: Center
# 
# Note: You can actually learn quite a bit more from this analysis, see Strogatz chapter 6. In fact, these eigenvalues can tell us about the nature of the local trajectories. 
# 

# ## Additional Resources
# 
# ### Stability and Eigenvalues of a linearized system
# 
# Steve Brunton at UW does dynamical systems research and has a great video that demonstrates how we make meaning of those eigenvalues.
# 
# [![](https://markdown-videos-api.jorgenkh.no/youtube/XXjoh8L1HkE?width=720&height=405)](https://inv.tux.pizza/watch?v=XXjoh8L1HkE)
# 
# ### Eigenvalues, Computationally 
# 
# We can use `np.linalg.eig()` to find the eigenvalues (and normalized eigenvectors) of a matrix which we represent as numpy array. Below is some doe that does this (note the imaginary unit is represented as $j$ in python):

# In[1]:


import numpy as np
A = np.array([[0,1],[-1,0]])
eigvals = np.linalg.eig(A)[0]
eigvecs = np.linalg.eig(A)[1]

print("eigenvalues:", eigvals)


# This can be super handy when you just need to do some quick characterization from the eigenvalues of a matrix. However, be warned - since you only get numerical answers you can lose quite a bit of the nuance that comes from if you had calculated these. We'll see how that can be an issue later in the semester when we tackle normal modes. 
# 
# ### Handwritten Notes
# 
# - [Linearization of ODEs](https://github.com/dannycab/phy415fall23/blob/main/content/assets/notes/Notes-Linearization_ODEs.pdf)
# - [Linearization example](https://github.com/dannycab/phy415fall23/blob/main/content/assets/notes/Notes-Linearization_Example.pdf)

# 
