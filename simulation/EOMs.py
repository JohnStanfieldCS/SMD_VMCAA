import numpy as np
import more_itertools as mit
from numpy import linalg as LA

# Dynamics Function
def dynamics(x,t,Mu):
    J2 = 1.08248e-3
    Re = 6378

    Rr = np.array([x[0],x[1],x[2]])
    R = np.reshape(Rr,(3,1))
    r = LA.norm(R)

    acell = (-3/2)*J2*(Mu/r**2)*((Re/r)**2)

    aJ2x = acell*((1-5*((R[2,0]/r)**2))*(R[0,0]/r))
    aJ2y = acell*((1-5*((R[2,0]/r)**2))*(R[1,0]/r))
    aJ2z = acell*((3-5*((R[2,0]/r)**2))*(R[2,0]/r))

    aTx = -(Mu/r**3)*R[0,0]
    aTy = -(Mu/r**3)*R[1,0]
    aTz = -(Mu/r**3)*R[2,0]


    ax = aTx + aJ2x
    ay = aTy + aJ2y
    az = aTz + aJ2z

    Xdot = np.empty((6,))

    Xdot[0] = x[3]
    Xdot[1] = x[4]
    Xdot[2] = x[5]
    Xdot[3] = ax
    Xdot[4] = ay
    Xdot[5] = az
    return Xdot