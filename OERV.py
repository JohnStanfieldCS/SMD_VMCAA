# make function for OE to RV
import numpy as np
def OE2RV(e,a,i,Omega,ArgP,Theta,Mu):
    p = a*(1-e**2)
    h = np.sqrt(p*Mu)

    x = (np.cos(np.deg2rad(Theta)))

    Rvector = np.array([[(np.cos(np.deg2rad(Theta)))],[(np.sin(np.deg2rad(Theta)))],[0]])

    posI = ((h**2)/Mu)*(1/(1+e*(np.cos(np.deg2rad(Theta)))))*Rvector
    velI = (Mu/h)*np.array([[-(np.sin(np.deg2rad(Theta)))],[e + (np.cos(np.deg2rad(Theta)))], [0]])

    T1 = np.matrix([[np.cos(np.deg2rad(ArgP)),np.sin(np.deg2rad(ArgP)),0],
                   [-np.sin(np.deg2rad(ArgP)),np.cos(np.deg2rad(ArgP)), 0],
                   [0, 0, 1]])
    T2 = np.matrix([[1, 0, 0],
                    [0, np.cos(np.deg2rad(i)), np.sin(np.deg2rad(i))],
                    [0, -np.sin(np.deg2rad(i)), np.cos(np.deg2rad(i))]])
    T3 = np.matrix([[np.cos(np.deg2rad(Omega)), np.sin(np.deg2rad(Omega)), 0],
                    [-np.sin(np.deg2rad(Omega)), np.cos(np.deg2rad(Omega)), 0],
                    [0, 0, 1]])
    DCM = T1 * T2 * T3 
    T = np.transpose(DCM)
    
    position = T * posI
    velocity = T * velI
    return position, velocity