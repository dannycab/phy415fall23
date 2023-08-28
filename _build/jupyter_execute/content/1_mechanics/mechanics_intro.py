#!/usr/bin/env python
# coding: utf-8

# # Intro to Classical Mechanics

# Welcome to Mathematical Modeling in physics! Our first unit will focus on Classical Mechanics and Ordinary Differential Equations (ODEs). Classical Mechanics is all about the motion of macrosopic objects, typically ones that are moving slow enough so that we can ignore special relativity. In particular, we are interested in systems that obey Newton's second law:
# 
# 
# $$\mathbf{F} = \frac{d\mathbf{p}}{dt} = \dot{\mathbf{p}}$$
# 
# or equivalently (if m is constant):
# 
# $$\mathbf{F} = m \frac{d\mathbf{r}}{dt^2} = m\ddot{\mathbf{r}}$$
# 
# Here we're using dot notation to mean derivatives with repsect to time. We'll continue to see this notation through this course.
# 
# The key thing to note here is that both of these equations are statements of **ordinary differential equations**. A huge portions of problems in physics boil down to differential equations, its probably more difficult to think of physics problems that aren't differential equations than ones that are. Broadly speaking, differential equations are equations of some **unkown** function and its derivatives. Often we are concerned with the form and/or behavior of this unknown function. In terms of newtons laws, if we are able to solve the differential equation $\mathbf{F} = m\ddot{\mathbf{r}}$, then we get some function $\mathbf{r}(t)$ that tells us exactly how our system evolves in time.
# 
# 
# ### Interpreting the statement of ODEs
# 
# A nice way to think of differential equations is as a set of instructions for how a function should change in time. For example, consider the first order ODE:
# 
# $$
# \dot{x} = x
# $$
# 
# This equation is saying that the function $x(t)$ should change according to what its current value is. We can also think of $\dot{x}$ as the velocity of function $x(t)$, so this equation is also saying that the velocity of $x(t)$ needs to be equal to its current position at all times, or that when we take a derivative of this function we get itself back. The function $e^t$ has this property, so it might be our go-to guess for the solution of this system. Since this equation is [seperable](https://math.libretexts.org/Courses/Monroe_Community_College/MTH_211_Calculus_II/Chapter_8%3A_Introduction_to_Differential_Equations/8.3%3A_Separable_Differential_Equations), we can solve it exactly by integrating:
# 
# $$
# \int \frac{dx}{x} = \int dt \implies \log(x(t)) = t + c
# $$
# 
# $$
# \implies x(t) = e^{(x + c)} = Ae^t \text{ if we let } A = e^c
# $$
# 
# Our guess at a solution was close, but the actual solution ended up with an extra $A$ term. In fact we've found **infinitley many** solutions, or the **general solution** since we don't know the value of $A$ that came from the integration constant.  Think for second about how we might go about finding what $A$ is.
# 
# ### Initial Conditions
# 
# To find $A$, we would need to know what $x(t=0)$ is. Let's say for the particular solution we're interested in has $x(t=0) = x_0$. Then its straightforward to solve for $A$:
# 
# $$
# x(t=0) = x_0 = Ae^0 = A \implies A = x_0 \implies x(t) = x_0e^t
# $$
# 
# So we've found a **specific** or **unique** solution to this ODE. In general, for an $n$ th-order (the highest order is of $n$ th degree) ODE, you need $n$ iniial conditions to find a specific solution. We'll see why this is in the coming weeks. 
# 
# ### A note on differentiability
# 
# When we are concerned with differential equations that show up in classical mechanics, we often secretly make the assumption that the function that we are looking for is differentiable in the first place, i.e. that the function is sufficiently smooth so that $\lim_{t\to 0} \frac{\Delta \mathbf{r}}{\Delta t}$ exists. For the systems we'll concern ourselves with in this class, we will take this for granted. Some differential equation models do run into this being an issue though, such as in fracture mechanics or models of swarming behavior, where one needs to employ what is called nonlocal analysis, which is a really interesting bit of math that we just don't have the time to cover in this class sadly.
# 
# But before we can start modeling more or less whatever we'd like with ODEs, we need to get familiar with some different frames of reference, or coordinate systems that solutions to ODEs often live in. That leads us to our [first in-class activity](https://valentine-alia.github.io/phy415fall23/content/1_mechanics/frames.html).
