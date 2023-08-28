#!/usr/bin/env python
# coding: utf-8

# # 31 Aug 23 - Frames and Coordinates

# ## What is a Frame?
# 
# A **Frame of Reference**, **Reference Frame**, or simply **Frame** is a set of coordinates. These coordinates describe where things are. 
# 
# 
# An **inertial frame** is a Frame where newtons first law holds, which means that in this frame a net force of zero means an acceleration of zero. In practice, this means that if you have two frames that are moving at a constant velocity relative to each other (without rotation), these are inertial frames.

# ### Relative Velocities in cartesian coordinates
# 
# Suppose you're walking down shaw lane eager to get to BPS for your favorite physics class at constant velocity $v_A$ when you notice a [squirrel](https://www.instagram.com/qualitysquirrelsofmsu/) sitting stationary on the sidewalk $d$ meters in front of you. You're a physics major so you naturally feel the urge to unnececarily mathematically analyze this situation using reference frames. 
# 
#  Let's call your reference frame $A$ and the squirrel's $B$. We'll ignore height differences between you and the squirrel.

# ### Questions
# 
# A note on notation: $r_{A/B}$ means "the position of **object** $A$ in **frame** $B$," or simply "the position of $A$ relative to $B$."
# 
# 
# 
# 
# <img src="https://raw.githubusercontent.com/valentine-alia/phy415fall23/main/content/assets/squirrel1.png" alt="squirrel1" width=500px/>
# 
# 
# **&#9989; Do this** 
# 
# Answer the following Questions:
# 
# 1. What is the squirrels position in your frame, $r_{B/A}$?
# 2. What is your position in the squirrel's frame, $r_{A/B}$?
# 3. What is your velocity in your frame, $\dot{r}_{A/A} = v_{A/A}$?
# 4. What is the sqirrel's velocity in your frame, $v_{B/A}$?
# 5. What is your velocity in the squirrels frame, $v_{B/A}$?
# 6. Suppose that the squirrel starts walking to the right at the same velocity that you are walking at. What is $v_{B/A}$ now?
# 
# Hopefully these are intuitive from what you've learned back in PHY 183, but there are subtleties to the math you just did. Is there a relationship between $v_{B/A}$ and $v_{A/B}$?
# 
# In general, for inertial frames $A,B,$ and object $C$ one has the following:
# 
# $$\mathbf{r}_{A/C} = \mathbf{r}_{A/B} + \mathbf{r}_{B/C} $$
# 
# taking a derivative gives:
# 
# $$\dot{\mathbf{r}}_{A/C} = \dot{\mathbf{r}}_{A/B} + \dot{\mathbf{r}}_{B/C} $$
# 
# This derivative works out so simply only because the **unit vectors are fixed in cartesian coordinates**. That is, if we write a generic vector in one of these frames as $\mathbf{r} = x\mathbf{\hat x} + y\mathbf{\hat y} + z \mathbf{\hat z}$, and then take a time derivative, we simply get $\dot{\mathbf{r}} = \frac{d}{dt} \mathbf{r} = \frac{dx}{dt}\mathbf{\hat x} + \frac{d\mathbf{\hat x}}{dt} x + \frac{dy}{dt}\mathbf{\hat y} + \frac{d\mathbf{\hat y}}{dt} y + \frac{dz}{dt}\mathbf{\hat z} + \frac{d\mathbf{\hat z}}{dt} z = \dot{x}\mathbf{\hat x} + \dot{y}\mathbf{\hat y} + \dot{z} \mathbf{\hat z}$ because the derivatives of the unit vectors vanish. Later, you'll figure out what happens when you have non-constant unit vectors.
# 
# Let's use these transformations in a problem.
# 
# A second squirrel appears, which we'll call squirrel $C$. This scares the first squirrel into running toward you, while the new squirrel runs away.
# 
# 
# 
# <img src="https://raw.githubusercontent.com/valentine-alia/phy415fall23/main/content/assets/squirrel2.png" alt="squirrel1" width=650px/>
# 
# 
# ### Questions
# 
# **&#9989; Do this** 
# 
# Answer the following question:
# 
# What is the velocity of $B$ relative to $C$?

# ### The Galilean Transformation
# 
# We just did an example of a **Galilean Transformation**. Traditionally, if we have a frame $B$ that with moves with constant velocity $v_{B/A}$ with respect to frame $A$, we re-write the above equations as the following:
# 
# $$\mathbf{v}_B = \mathbf{v}_A - \textbf{v}_{B/A}$$
# 
# $$\mathbf{r}_B = \mathbf{r}_A - \mathbf{v}_{B/A} t$$
# 
# Where we have taken $_A$ to mean $_{C/A}$ and $_B$ to mean $_{C/B}$. Also note that since we are ignoring relativistic effects, we also have that:
# 
# $$t_B = t_A$$
# 
# ### Checking the physics
# 
# This is all well and good, but we should make sure to check that newtonian mechanics works the same in both of these frames, that they are really inertial frames. 
# 
# **&#9989; Do this** 
# 
# In your group, show that forces experienced in frame $A$ are the same as forces experienced in frame $B$. (Hint: $v_{B/A}$ is constant)

# 

# ## Forces in polar coordinates
# 
# Many problems in physics require the use of non-cartesian coordinates, such as the Hydrogen atom or the two-body problem. One such coordinate system is **polar coordinates**. In this coordinate system, any vector $\mathbf{r}\in \mathbb{R}^2$ is described by a distance $r$ and angle $\phi$ insead of cartesian coordinates $x$ and $y$. The following four equations show how points transform in these coordinate systems.
# 
# $$
# x = r\cos \phi \hspace{1in} y = r\sin \phi
# $$
# 
# $$
# r = \sqrt{x^2 + y^2} \hspace{1in} \phi = \arctan(y / x)
# $$
# 
# This also let's us write kinetic energy as $T = \frac{1}{2}m(\dot{r} + r^2\dot{\phi}^2)$.
# 
# 
# We'd like to know how to write down Newton's second law in this coordinate system, but this is not as simple as before because the unit vectors in polar coordinate are NOT constant. We'll denote the unit vectors for polar coordinates by $\hat{\mathbf{r}}$ and $\hat{\boldsymbol{\phi}}$. $\hat{\mathbf{r}}$ points in the direction of increasing $r$ with $\phi$ fixed, and similarly $\hat{\boldsymbol{\phi}}$ points in the direction of increasing $\phi$ with $r$ fixed.
# 
# 
# However, this doesen't stop us from being able to break down a net force into its components along each unit vector:
# 
# $$
# \mathbf{F} = F_r \hat{\mathbf{R}} + F_\phi \hat{\boldsymbol{\phi}}
# $$
# 
# And the second law still holds:
# 
# $$
# \mathbf{F} = m\ddot{\mathbf{r}}
# $$
# 
# It would be very useful if we had expressions for $F_r$ and $F_\phi$ in terms of $r$ and $\phi$. Toward finding these, we can start by writing:
# 
# $$
# \mathbf{r} = r\hat{\mathbf{r}}
# $$
# 
# 
# ### Task
# 
# **&#9989; Do this** 
# 
# Find $\dot{\mathbf{r}}$ by differentiating $\mathbf{r}$ with respect to time. (see hint below)
# 
# 
# 
# **&#9989; Do this** 
# 
# 
# 
# Find $\ddot{\mathbf{r}}$ by differentiating $\dot{\mathbf{r}}$ with respect to time. Then find $F_r$ and $F_\phi$. (see hint below)
# 
# 
# <!--\dot{\mathbf{r}} = \dot{r}\hat{r} + r\dot{\phi}\hat{phi} -->
# <!-- -->
# 
# 
# Hint: During these problems, you'll need to find expressions for $\frac{d\hat{\mathbf{r}}}{dt}$ and $\frac{d\hat{\boldsymbol{\phi}}}{dt}$, which [these pictures](https://raw.githubusercontent.com/valentine-alia/phy415fall23/main/content/assets/frames_hint.pdf) might help with.
# 

# #### Angular momentum
# 
# One of the powerful things you get from using this coordinate system is a handy way to represent angular momentum:
# 
# $$
# |\mathbf{L}| = |\mathbf{r} \times \mathbf{p}| = |mr^2\dot{\phi}|
# $$
# 
# In the interest of time we won't go through the whole calculation to arrive at this, but this is handy to know.

# ### (time permitting) Non-Inertial Frames
# 
# Broadly speaking, non-inertial frames are frames that undergo some sort of acceleration. In general for inertial frame $A$ and non-inertial frame $B$, we can write:
# 
# $$r_B = r_A - r_{B/A}$$
# 
# $$v_B = v_A - v_{B/A}$$
# 
# as before, as well as:
# 
# $$\ddot{r}_B = \ddot{r}_{A} - \ddot{r}_{B/A}$$
# 
# Interestingly, this means a new (ficticious) force has sprung into being, equal to $-m\ddot{r}_{B/A}$ ! This lets us write newton's second law for frame B as: 
# 
# $$m\ddot{r}_{B} = F -m\ddot{r}_{B/A}$$

# ### Leaning on a bus problem
# 
# Suppose you're standing on a bus that is accelerating forward with constant acceleration $r_{B/A}$. If we approximate you as a pendulum, what angle should you lean at so you can stay at equillibrium without having to exert any force to stay at that angle?
# 
# **&#9989; Do this** 
# 
# Solve this problem using the the as a non-inertial frame. [Solution](https://raw.githubusercontent.com/valentine-alia/phy415fall23/main/content/assets/bus_soln.pdf)

# ### Forces in Rotating Frames
# 
# For intertial frame A and non-inertial, rotating frame B, rotating at an angular velocity of $\mathbf{\Omega}$ relative to A, we can write the second law as:
# 
# $$
# m\ddot{\mathbf{r}} = \mathbf{F} + 2m\dot{\mathbf{r}}\times \mathbf{\Omega} + m (\mathbf{\Omega}\times \mathbf{r}) \times \mathbf{\Omega}
# $$
# 
# Where $\mathbf{F}$ is any "standard" forces from inertial frames, $2m\dot{\mathbf{r}}\times \mathbf{\Omega}$ is the Coriolis force, and $m (\mathbf{\Omega}\times \mathbf{r}) \times \mathbf{\Omega}$ is the centrifugal force.
