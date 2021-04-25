import numpy as np
import math as mt

def rv2LL(position2):
    r = np.linalg.norm(position2)
    x = (position2[0])/r
    y = (position2[1])/r
    z = (position2[2])/r
    deg = 180/np.pi

    lat = np.rad2deg(np.arcsin(z))

    precalc_long = ((np.arccos(x/np.cos(mt.radians(lat))))*deg)
    if y > 0:
        long = precalc_long
    elif y <= 0:

        long = 360 - precalc_long


    return lat, long
