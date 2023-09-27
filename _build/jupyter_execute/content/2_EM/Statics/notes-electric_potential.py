#!/usr/bin/env python
# coding: utf-8

# # 3 Oct 23 - Notes: Electric Potential - a scalar field
# 
# We've seen that there's a lot of challenges with solving field problems where the fields are vectors and described by partial differential equations. The electric and magnetic field are vector fields that have a size and direction are every points in space. They are described by a set of 4 partial differential equations, [Maxwell's Equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations). In Cartesian coordinates, these equations are described by 8 coupled partial differential equations.
# 
# ## Electrostatics
# 
# In electrostatic situations, where charges don't move, we've seen that the equations that describe the electric field are simplified to:
# 
# $$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$$
# 
# $$\nabla \times \vec{E} = 0$$
# 
# In general, in Cartesian coordinates, these are still four partial differential equations. However, the electric field is [curl-less](https://en.wikipedia.org/wiki/Curl_(mathematics)), so we can write it as the gradient of a scalar field, $V$:
# 
# $$\vec{E}(x,y,z) = -\nabla V(x,y,z)$$
# 
# We might prefer to work with this scalar field, $V$, rather than the vector field, $\vec{E}$, because it is a simpler object to work with. There's a number of tools we can use to find the potential and then we take the gradient to find the electric field.

# ### Electric Potential
# 
# Parth G has a really nice video on the conceptual elements of electric potential, we will concern ourselves with more mathematical aspects as we move forward.
# 
# [![Electric Potential](https://markdown-videos-api.jorgenkh.no/youtube/7rjAtuwxrEA?width=720&height=405)](https://inv.tux.pizza/watch?v=7rjAtuwxrEA)
# 
# 
# The [electric potential](https://en.wikipedia.org/wiki/Electric_potential) is the scalar field that we have developed. One thing to note about it, is that it is only defined up to a constant. That is because when we take the gradient, and constant will drop out. This is really important when stitching together solutions from multiple sources. They need to all have the same "zero of potential."
# 
# With the definition, $\vec{E}(x,y,z) = -\nabla V(x,y,z)$, we can conclude the following:
# 
# $$\nabla \cdot \vec{E} = \nabla \cdot (-\nabla V) = -\nabla^2 V = \frac{\rho}{\epsilon_0}$$
# 
# where $\nabla^2$ is the [Laplacian operator](https://en.wikipedia.org/wiki/Laplace_operator). This is [Poisson's Equation](https://en.wikipedia.org/wiki/Poisson%27s_equation), a well-studied second order partial differential equation. When used in electrostatics, it is a central equation for solving for the electric potential. In addition, we can integrate to show that:
# 
# $$\Delta V = -\int \vec{E} \cdot d\vec{l}$$
# 
# where the line integral is taken along a path from one point to another. For the electric field, this is independent of path, so we can write:
# 
# $$\Delta V = -\int_{\vec{r}_1}^{\vec{r}_2} \vec{E} \cdot d\vec{l} = V(\vec{r}_2) - V(\vec{r}_1)$$
# 
# And
# 
# $$\oint \vec{E} \cdot d\vec{l} = 0$$
# 
# which is a direct results of applying Stokes' Theorem to the curl-less electric field, and indicates that the electric field is conservative.

# ## Getting to Laplace's Equation
# 
# Poisson's Equation is a description of a scalar potential (e.g., the electric potential) and how it relates to sources of the potential (e.g., charges). This is a **local** description of the field. At every point, the Laplacian can be computed (for well-behaved functions) and it indicates a source or lack of sources. For example, in empty space with no charges, the Laplacian is zero everywhere. 
# 
# So if we imagine setting up charges far from the place we are interested in finding the electric potential, we have an equation that is describes that space.
# 
# $$\nabla^2 V = 0$$
# 
# This is Laplace's equation and is a commonly occurring equation in physics. In fact, as we saw here, it shows up anytime we find local situations where the charges are absent. So the idea is that charges are far away setting the potential at the boundaries (hence, calling these **[boundary value problems](https://en.wikipedia.org/wiki/Boundary_value_problem)**). The idea is that the PDE is solved in the region of interest often giving some general solution in the form of an infinite sum. The boundary conditions are then used to determine the coefficients in the solution, giving a unique solution. Because Laplace's equation is a linear PDE, the superposition principle applies, so we can add solutions together to get new solutions.
# 
# ### A typical problem
# 
# It might seem odd to have an equation that is everywhere equal to zero and somehow suggest it produces non-zero solutions. But remember that it is a PDE that describes the second derivatives of this scalar function,
# 
# $$\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2} = 0$$
# 
# It turns out there's lots of functions that will satisfy that differential equation. And it's mostly a matter of if the function fits the boundary conditions. Let's look at a typical problem.
# 
# ![Typical Laplace's Equation Problem](https://www.physics.uoguelph.ca/sites/default/files/uploads/fig10_1-parallel-plates.jpg)
# *Image from [University of Guelph](https://www.physics.uoguelph.ca/chapter-10-laplaces-equation)*
# 
# Here is a "gutter" where the electric potential for different sides of the gutter are set. Laplace's equation applies inside the gutter. So the idea is to find a solution that satisfies Laplace's equation and the boundary conditions. We will develop this solution in class, but the representative results look like this:
# 
# ![Typical Laplace's Equation Solution](https://www.physics.uoguelph.ca/sites/default/files/uploads/fig10_2_potential-plates.jpg)
# *Image from [University of Guelph](https://www.physics.uoguelph.ca/chapter-10-laplaces-equation)*

# ## Separation of Variables
# 
# One of the key analytical tools that we have for Laplace's Equation is the [separation of variables](https://en.wikipedia.org/wiki/Separation_of_variables) method of solving PDEs. We posit an ansatz in which the solution is a product of functions of the individual variables. For example, in Cartesian coordinates, we might write:
# 
# $$V(x,y,z) = X(x)Y(y)Z(z)$$
# 
# And then we plug that into Laplace's equation and see if we can find solutions. In this case, we get:
# 
# $$\nabla^2 V = YZ\frac{d^2 X}{dx^2} + XZ\frac{d^2 Y}{dy^2} + XY\frac{d^2 Z}{dz^2} = 0$$
# 
# which we divide by $XYZ$ to obtain the following expression: 
# 
# $$\frac{1}{X}\frac{\partial^2 X}{\partial x^2} + \frac{1}{Y}\frac{\partial^2 Y}{\partial y^2} + \frac{1}{Z}\frac{\partial^2 Z}{\partial z^2} = 0$$
# 
# Here each partial derivative is a of a pure function of a single variable. So we can conclude that each term is a constant that sum to zero. We can write this as:
# 
# $$\frac{d^2 X}{d x^2} = -k_x^2X$$
# $$\frac{d^2 Y}{d y^2} = -k_y^2Y$$
# $$\frac{d^2 Z}{d z^2} = -k_z^2Z$$
# 
# where $k_x^2 + k_y^2 + k_z^2 = 0$. We have converted our problem to a set of 3 ODEs that we know how to solve. We can then solve each of these equations separately and show a general solution is:
# 
# $$X(x) = Ae^{ik_xx} + Be^{-ik_xx}$$
# $$Y(y) = Ce^{ik_yy} + De^{-ik_yy}$$
# $$Z(z) = Fe^{ik_zz} + Ge^{-ik_zz}$$
# 
# where $A,B,C,D,E,F,G$ are constants. We can then use the boundary conditions to determine the constants. Notice we wrote these as complex exponentials, those are sinusoidal or exponential solutions depending on if the resulting $k$'s are real or complex. The electric potential is a real measurable quantity.
# 
# This general approach is well known and well-traveled territory. It's working with these boundary conditions that can be tricky, and that we will practice. We will find that for most cases that we end up with infinite sums of these solutions. We will also find that we can use the [orthogonality of the solutions](https://en.wikipedia.org/wiki/Orthogonal_functions) to simplify the solutions.
# 
# **We should not suggest that every PDE can be solved with separation of variables, but rather that:**
# * Separation of variables is a powerful tool for solving PDEs that you can try, but it might not work.
# * It is a tool that can produce general solutions to Laplace's Equation when the Laplacian is separable in the given coordinate system.
# * It cannot be used for some problems (e.g., when the boundary conditions cannot be expressed as [Neumann](https://en.wikipedia.org/wiki/Neumann_boundary_condition) or [Dirichlet](https://en.wikipedia.org/wiki/Dirichlet_boundary_condition) boundary conditions).
# 
# ### Other Coordinate Systems
# 
# It turns out the trick of positing a solution that is a product of functions of the individual variables works in other coordinate systems as well. For example, in cylindrical coordinates, we might write:
# 
# $$V(r,\theta,z) = R(r)\Theta(\theta)Z(z)$$
# 
# Or in spherical coordinates, we might write:
# 
# $$V(r,\theta,\phi) = R(r)\Theta(\theta)\Phi(\phi)$$
# 
# It turns out both of these are separable in their respective coordinate systems. We will work through some examples of spherical coordinates in class as it forms the basis of the [Multipole Expansion](https://en.wikipedia.org/wiki/Multipole_expansion), which is a critical mathematical tool with wide applications.
# 
# This idea of funding general solutions to Laplace's equation in known orthogonal coordinate systems remains incredible common. Experimental setups and theoretical models often have situations where Laplace's equation is relevant and there is a symmetry that can be exploited to find solutions. Laplace's equation is separable in 13 coordinate systems. You can find some of the more [exotic equations and coordinate systems here](https://en.wikipedia.org/wiki/Orthogonal_coordinates#Table_of_three-dimensional_orthogonal_coordinates). Check out the [Prolate Spheroidal coordinates](https://en.wikipedia.org/wiki/Prolate_spheroidal_coordinates), which are used in nuclear physics when the nucleus is deformed.
# 
# ![Prolate Spheroidal Coordinates](https://upload.wikimedia.org/wikipedia/commons/b/be/Prolate_spheroidal_coordinates.png)
# 

# ## Additional Resources
# 
# ### Textbook Chapter
# 
# The University of Guelph provides free notes in physics. Here's the [relevant chapter on Laplace's Equation](https://www.physics.uoguelph.ca/chapter-10-laplaces-equation). It is also where some of the figures were taken from.
# 
# ### Videos Derivations
# 
# Steve Brunton at Washington has some really great videos on the derivations associated with PDEs like those above.
# 
# #### Possion's and Laplace's Equation
# 
# [![Possion's and Laplace's Equation](https://markdown-videos-api.jorgenkh.no/youtube/nmvs0vrBT18?width=720&height=405)](https://inv.tux.pizza/watch?v=nmvs0vrBT18)
# 
# #### Separation of Variables
# [![Separation of Variables](https://markdown-videos-api.jorgenkh.no/youtube/VjWtMl6vQ3Q?width=720&height=405)](https://inv.tux.pizza/watch?v=VjWtMl6vQ3Q)
# 
# ### Handwritten Notes
#  - [Electric Potential](../../assets/notes/Notes-Electric_Potential.pdf)
#  - [Separation of Variables](../../assets/notes/Notes-Separation_of_Variables_Cartesian.pdf)
#  - [Separation of Variables (Spherical Coordinates)](../../assets/notes/Notes-Separation_of_Variables_Spherical.pdf)
#  - [Multipole Expansion](../../assets/notes/Notes-Multipole_Expansion.pdf)

# 
