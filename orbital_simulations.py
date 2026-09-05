import numpy as np
import matplotlib.pyplot as plt
# Define values related to earth and satellite in SI units
G = 6.67e-11
M = 5.972e24
m = 1000
R_earth = 6.371e6
Altitude = 8e5
#Define initial position and velocity
r0 = R_earth + Altitude
x = r0
y = 0
v0 = np.sqrt(G*M/r0)
vx = 0
vy = v0
#Introduce time variable and steps
dt = 1       # Satellite takes 1 second to complete 1 step
steps = 10000
#Create x and y array
x_values = np.zeros(steps)
y_values = np.zeros(steps)
for i in range(steps):
   r = np.sqrt(x**2 + y**2)  # r is distance of satellite from earth(0,0) or r is position vector
   ax = -G*M*x/r**3          # acceleration in x and y direction
   ay = -G*M*y/r**3
   vx = vx + ax*dt           # new velocity as satellite moves
   vy = vy + ay*dt
   x = x + vx*dt             # new position as satellite moves
   y = y + vy*dt
   x_values[i] = x           # replace the zeroes in the array created earlier with actual values
   y_values[i] = y
   v = np.sqrt(vx**2 + vy**2) # velocity vector
   KE_per_m = 0.5*v**2        # Energy formulas
   PE_per_m = -G*M/r
   E_total = KE_per_m + PE_per_m
print(f"Average Energy = {np.mean(E_total)} J/kg")
print(f"Energy is negative? {np.mean(E_total) < 0} -> so bound orbit")
r = np.sqrt(x_values**2 + y_values**2)      # orbit radius/ radius vector
print(f"Average radius = {np.mean(r)}")     # calculates average orbital radius
import math 
r_avg = np.mean(r)
T = 2*math.pi*math.sqrt(r_avg**3/(G*M))     # calculate time period
print(f"Time period = {T} seconds = {T/60} minutes")
plt.plot(x_values, y_values)                # plot graph using matplotlib 
plt.scatter(0,0, label = "Earth")       
plt.xlabel("x position(m)")
plt.ylabel("y position(m)")
plt.title("Satellite orbit around Earth")
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()
plt.savefig('orbit.png')
print("Orbit saved!!!!! YAYYYY!!!!")
