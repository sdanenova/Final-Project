import numpy as np
import math
from scipy import integrate
import matplotlib.pyplot as plt

global Lx, Lz,  Bz_min, Bz_max, B_lobe,  B_e, x0

#Parameters from the model to build magnetic field lines
Lx = 0.082
Lz = 0.741455
Bz_min = 5.495
Bz_max = 10.02
B_lobe = 34.91
B_e = -30600
x0 = - 10.0

#function that defines the equation for ODE
def bysyst(t, y):
    dy = np.zeros((1,1))
    

    global  Lx, Lz,  Bz_min, Bz_max, B_lobe,  B_e, x0
    

    #f1 = B_dip_x
    #f2 = B_dip_z
    #f3 = B_PS_x
    #f4 = B_PS_z
    
    f1 = (((B_e)*((1/math.sqrt((y**2)+(t**2)))**3)*(3*y*t))/((y**2)+(t**2)))
    f2 = (((B_e)*((1/math.sqrt((y**2)+(t**2)))**3)*((2*(t**2)-(y**2))/((y**2)+(t**2)))))*((0.5* (1 + math.tanh( (y) +9) ) ))
    f3 = (B_lobe*math.tanh(t/Lz));
    f4 = (Bz_min+(0.5)*(Bz_max-Bz_min)*(1+math.tanh((-y + x0)/ Lx)))




    dy = (f1 + f3)/(f2 +f4)
    return dy

t0, t1 = 0, 3                # start and end
t1 = np.linspace(t0, t1, 100) 
t = np.array(t1) # the points of evaluation of solution
y0 = [x0, -4.8967]                   # initial value
y1 = np.zeros((len(t), len(y0)))
y = np.array(y1)  # array for solution
y[0, :] = y0
r = integrate.ode(bysyst).set_integrator("dopri5")  # choice of method
r.set_initial_value(y0, t0)   # initial values
for i in range(1, t.size):
   y[i, :] = r.integrate(t[i]) # get one more value, add it to the array
   if not r.successful():
       raise RuntimeError("Could not integrate")
plt.plot(t, y) #plotting magnetic field lines as a function of t and y 
plt.show()