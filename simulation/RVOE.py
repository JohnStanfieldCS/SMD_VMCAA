import numpy as np
import more_itertools as mit

def RV2OE(position,velocity,Mu):
    pos = np.array(position)
    vel = np.array(velocity)

    v = np.linalg.norm(vel)
    r = np.linalg.norm(pos)

    dotV = mit.dotproduct(pos,vel)
    RadialV = dotV/r

    pos2 = np.reshape(pos, (1,3))
    vel2 = np.reshape(vel, (1,3))

    h = np.cross(pos2,vel2)
    H = np.linalg.norm(h)

    i = np.rad2deg(np.arccos(h[0,2]/H))

    K = np.array([0, 0, 1])
    n = np.cross(K,h)
    n3 = np.reshape(n, (3,1))
    N = np.linalg.norm(n)

    if n[0,2] >= 0:
        Omega = np.rad2deg(np.arccos(n[0,0]/N))
    elif n[0,2] < 0:
        Omega = 360.0 - np.rad2deg(np.arccos(n[0,0]/N))

    e = (1/Mu)*((((v**2)-(Mu/r))*pos)-((r*RadialV)*vel))
    ec = np.reshape(e, (1,3))
    E = np.linalg.norm(ec)

    dotA = mit.dotproduct(n3,e)
    NE = N*E
    if ec[0,2] >= 0:
        w = np.rad2deg(np.arccos(dotA/NE))
    elif ec[0,2] < 0: 
        w = 360 - np.rad2deg(np.arccos(dotA/NE))

    dotT = mit.dotproduct(e,pos)
    Er = E*r
    if RadialV >= 0:
        Theta = np.rad2deg(np.arccos(dotT/Er))
    elif RadialV < 0:
        Theta = 360 - np.rad2deg(np.arccos(dotT/Er))

    Rp = ((H**2)/Mu)*(1/(1+E))
    Ra = ((H**2)/Mu)*(1/(1-E))

    a = 0.5 * (Rp + Ra)
    



    return(E,a,i,Omega,w,Theta)