import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint

print("IMPORT")
t = np.linspace(0, 100)
alpha = 0.2925
beta = 0.328879
gamma = 0.375
mu_h = 23/500000
delta = 0.0323

def derivatives(arc,t): 
    X, Y, Z, T = arc
    dx = mu_h*(1-X)-alpha*X*Z
    dz = gamma*(1-Z) * Y - delta * Z
    dy = alpha * X * Z - beta * Y
    dT = 0
    return dx, dy, dz
  
# values of time 
t = np.linspace(0, 5) 
  
# solving ODE 
y0 = 0.2, 0.8, 1
y = odeint(derivatives, y0, t) 
  
# plot results
plt.plot(t, y)
plt.xlabel("Time") 
plt.ylabel("Y")
plt.show()
print("PROGRAM EXECUTED")