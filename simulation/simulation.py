import sys
import json
import requests
import numpy as np
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as LA
from OERV import OE2RV
from RVOE import RV2OE
from EOMs import dynamics
from latlong import rv2LL
from plottingfunct import plotter
from  apiFUNC import apiCALL

# Basic Parameters
J2 = 0.00108248
Mu = 398600.4
RE = 6378.145
Re = 6378.145

url = "https://db9a57801208.ngrok.io/api/SatID"
response = requests.get(url)
SatID = str(response.json())

(checker,SatNum,eccen,inc,ArgPer,MeanAnom,RAAN,MMotion) = apiCALL(SatID)

if SatID == SatNum:
    e = (0.0 + float(eccen))/10000000
    i = float(inc)
    ArgP = float(ArgPer)
    MeanA = float(MeanAnom)
    Omega = float(RAAN)
    MeanMot = (float(MMotion) * (2*np.pi))/86400
    a = (Mu/MeanMot**2)**(1/3)
    Theta = np.rad2deg(np.arccos(-e))


# time discretization
ti = 0.0
T = ((2*np.pi)/(np.sqrt(Mu)))*a**(3/2)
dt = 150
tspan = np.linspace(ti,T,dt)

# Convert orbital elements from the API to cartesion vectors
[position,velocity] = OE2RV(e,a,i,Omega,ArgP,Theta,Mu)
X0 = np.array([position[0,0],
                position[1,0],
                position[2,0],
                velocity[0,0],
                velocity[1,0],
                velocity[2,0]])

# Solver/Integrator
xs = odeint(dynamics, X0, tspan, args=(Mu,),atol=1E-8,rtol=1E-8)
endpoint = len(tspan)
i = 0
eccentricity = []
semimajor = []
inclination = []
RAAN = []
ArgPer = []
Tanom = []
lat2 = []
long2= []
Latitude = []
Longitude = []
for i in range(0,endpoint):
    position = np.array([xs[i,0],xs[i,1],xs[i,2]])
    velocity = np.array([xs[i,3],xs[i,4],xs[i,5]])

    # Convert simulation position & velocity values to orbital elements

    [e,a,i,Omega,ArgP,Theta] = RV2OE(position,velocity,Mu)
    [lat,long] = rv2LL(position)

    eccentricity.append(e)
    semimajor.append(a)
    inclination.append(i)
    RAAN.append(Omega)
    ArgPer.append(ArgP)
    Tanom.append(Theta)
    
    Latitude.append(lat)
    Longitude.append(long)
    i =+ 1

tolerance = 100
k = 0
curve_num = 0
longPREV = Longitude[0]

lon0 = []
lat0 = []

lon1 = []
lat1 = []

lon2 = []
lat2 = []

lon3 = []
lat3 = []


for k in range(0,endpoint-1):
    meas = abs(Longitude[k+1] - longPREV)
        
    if abs(Longitude[k+1] - longPREV) > tolerance:
        curve_num = curve_num + 1
    long_prev = Longitude[k]

    if curve_num == 0:
        lon0.append(Longitude[k])
        lat0.append(Latitude[k])

    if curve_num == 1:
        lon1.append(Longitude[k])
        lat1.append(Latitude[k])

    if curve_num == 2:
        lon2.append(Longitude[k])
        lat2.append(Latitude[k])

    if curve_num == 3:
        lon3.append(Longitude[k])
        lat3.append(Latitude[k])

    longPREV = Longitude[k]
    k = k + 1

latnlong = []
grndTdata = {
            "LAT_1": lat0,
            "LON_1": lon0,
            "LAT_2": lat1,
            "LON_2": lon1,
            "LAT_3": lat2,
            "LON_3": lon2,
            }
latnlong.append(grndTdata)
print(json.dumps(latnlong))
sys.stdout.flush()
