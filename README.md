# orbit_simulator
# Orbit Simulator 🛰️

A 2D orbital mechanics simulator built from scratch in Python using NumPy and Matplotlib.

I built this in 12th grade out of curiosity to understand why satellites stay in orbit and what escape velocity actually means.
![Orbit](orbital%201.png) 
### What it does
- Simulates Newton's Law of Gravitation: F = GMm/r²
- Solves orbits numerically by varying initial velocity (1.0v0 = circular, 1.3v0 = elliptical, 1.5v0 = hyperbolic escape)
- Calculates Specific Mechanical Energy (KE + PE in J/kg) to verify if orbit is bound (E<0) or unbound (E>0)
- Calculates time period of satellite

### Tech Stack
Python, NumPy, Matplotlib

### What I learned
Debugging numerical integration, energy conservation check, - small typo = satellite escaping to infinity

Made by a 17-year-old from Goa, India.
