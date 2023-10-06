#!/usr/bin/env python
# coding: utf-8

# # 26 Sept 23 - Notes: Maxwell's Equations

# ## Electromagnetic Phenomena
# 
# You have certainly experienced a wide variety of electromagnetic phenomena in your life -- both natural (e.g., a sun rise, a rainbow, your hair standing on end) and human-made (e.g., switching on a light, using a microwave, using a cell phone). We now know that we can explain many of those phenomenon using a set of four partial differential equations: [Maxwell's Equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations). These equations describe a new mathematical object: a [field](https://en.wikipedia.org/wiki/Field_(physics)). The models that we develop from this theory are still [Classical](https://en.wikipedia.org/wiki/Classical_physics) -- in that we don't consider quantum mechanical effects. Rather we treat the fields as continuous functions of space and time.
# 
# While this might not seem that this classical theory is still useful in modern research, it is often the basis for much of the work done in physics. In fact, some important fusion energy research uses [magnetic confinement](https://en.wikipedia.org/wiki/Magnetic_confinement_fusion), which is effectively a classical electromagnetic phenomenon. The South Korean experimental fusion reactor, [KSTAR](https://en.wikipedia.org/wiki/KSTAR), is an example of this type of research, and it recently [sustained temperatures of 100 million degrees Celsius](https://www.popularmechanics.com/science/energy/a41191247/koreas-fusion-reactor-sustained-temperatures-7-times-hotter-than-the-sun-for-30-seconds/).
# 
# ### Magnetic Confinement in Fusion Energy
# 
# [![Magnetic Confinement](https://markdown-videos-api.jorgenkh.no/youtube/PWCqwZoE0FY?width=720&height=405)](https://inv.tux.pizza/watch?v=PWCqwZoE0FY)
# 
# - Non-Commercial Link: [https://inv.tux.pizza/watch?v=PWCqwZoE0FY](https://inv.tux.pizza/watch?v=PWCqwZoE0FY)
# - Commercial Link: [https://youtube.com/watch?v=PWCqwZoE0FY](https://youtube.com/watch?v=PWCqwZoE0FY)
# 

# ## Developing a complete theory
# 
# The work to develop [Maxwell's Equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations) was substantial and involved not only theoretical developments but confirmations using experiments. A model of reality is only as good as its ability to predict the results of experiments, which classical electromagnetism does very well (up to the point of quantum phenomena). The resulting Maxwell Equations that describe the electric ($\mathbf{E}$) and magnetic ($\mathbf{B}$) fields (in vacuum) are given by:
# 
# $$
# \textbf{Differential Form:}
# $$
# 
# Gauss's Law for Electricity:
# 
# $$
# \mathbf{\nabla} \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
# $$
# 
# Gauss's Law for Magnetism:
# 
# $$
# \mathbf{\nabla} \cdot \mathbf{B} = 0
# $$
# 
# Faraday's Law of Electromagnetic Induction:
# 
# $$
# \mathbf{\nabla} \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
# $$
# 
# Ampère's Law with Maxwell's Addition:
# 
# $$
# \mathbf{\nabla} \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
# $$
# 
# $$
# \textbf{Integral Form:}
# $$
# 
# Gauss's Law for Electricity:
# 
# $$
# \oint \mathbf{E} \cdot d\mathbf{A} = \frac{1}{\varepsilon_0} \int \rho dV
# $$
# 
# Gauss's Law for Magnetism:
# 
# $$
# \oint \mathbf{B} \cdot d\mathbf{A} = 0
# $$
# 
# Faraday's Law of Electromagnetic Induction:
# 
# $$
# \oint \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int \mathbf{B} \cdot d\mathbf{A}
# $$
# 
# Ampère's Law with Maxwell's Addition:
# 
# $$
# \oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 \int \mathbf{J} \cdot d\mathbf{A} + \mu_0 \varepsilon_0 \frac{d}{dt} \int \mathbf{E} \cdot d\mathbf{A}
# $$
# 
# We will work with different aspects of these equations as we make different assumptions about the physical system.
# 
# 
# ### A comment on the development of this theory
# 
# During the development of Classical Electromagnetism, physics research was often lead by single individuals with small armies of technicians, specialists, drafters, secretarial staff, and the like. While presented as the intellectual work of a single person, the work was an effort by a number of underpaid and under-recognized people (including, at the time, women and non-white men) who are unnamed in many books. A classical, and non critical, view of the development appears below in the video, but also in Meyer's book [A History of Electricity and Magnetism](https://mitpress.mit.edu/9780262130707/a-history-of-electricity-and-magnetism/). A more nuanced view of how science develops and is negotiated appears in Traweek's book [Beamtimes and Lifetimes](https://en.wikipedia.org/wiki/Beamtimes_and_Lifetimes).
# 
# 
# #### The Mechanical Universe
# 
# This video from the [Mechanical Universe series](https://en.wikipedia.org/wiki/The_Mechanical_Universe) and tells the story of the development of this theory. The video is dated and sexist and the instructor's stories are similarly problematic. The video puts scientists on a pedestal. But, it is worth a watch, both to recognize the history as presented and to reckon with the issues that these perspectives have continued to perpetuate. 
# 
# [![Maxwell's Equations](https://markdown-videos-api.jorgenkh.no/youtube/SS4tcajTsW8?width=720&height=405)](https://inv.tux.pizza/watch?v=SS4tcajTsW8)
# 
# - Non-Commercial Link: [https://inv.tux.pizza/watch?v=SS4tcajTsW8](https://inv.tux.pizza/watch?v=SS4tcajTsW8)
# - Commercial Link: [https://youtube.com/watch?v=SS4tcajTsW8](https://youtube.com/watch?v=SS4tcajTsW8)

# 
