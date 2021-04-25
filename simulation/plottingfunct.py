import matplotlib.pyplot as plt 
import numpy as np
def plotter(xs):
       Re = 6378.145
       ti = 0.0
       tf = 2.0*5600.0
       dt = 150
       tspan = np.linspace(ti,tf,dt)

       fig = plt.figure(figsize=(18,6))
       ax1 = fig.add_subplot(211,projection='3d')

       ax1.plot(xs[:,0],xs[:,1],xs[:,2],'k', Label = 'Trajectory')
       IC = [[xs[0,0]],[xs[0,1]],[xs[0,2]]]
       ax1.plot(IC[0],IC[1],IC[2],'go',Label = 'Current Position') # plot point for initial cond.

       # Plot Central Body
       _u,_v = np.mgrid[0:2*np.pi:20j,0:np.pi:10j]
       _x = Re*np.cos(_u)*np.sin(_v)
       _y = Re*np.sin(_u)*np.sin(_v)
       _z = Re*np.cos(_v)
       ax1.plot_surface(_x,_y,_z,cmap ='Greys')
       
       # Plot Axes
       l = Re*2
       x,y,z = [[0,0,0],[0,0,0],[0,0,0]]
       u,v,w = [[l,0,0],[0,l,0],[0,0,l]]
       ax1.quiver(x,y,z,u,v,w,color='k')

       max_val = np.max(np.abs(xs))
       ax1.set_xlim([-max_val,max_val])
       ax1.set_ylim([-max_val,max_val])
       ax1.set_zlim([-max_val,max_val])

       ax1.set_xlabel(['X (km)'])
       ax1.set_ylabel(['Y (km)'])
       ax1.set_zlabel(['Z (km)'])
       ax1.set_title('Orbit Visualization')

       plt.legend()
       plt.show()
'''
       ax2 = fig.add_subplot(212,)
       altitude = np.sqrt(xs[:,0]**2 + xs[:,1]**2 + xs[:,2]**2) - Re
       ax2.plot(tspan/3600,altitude)
       ax2.set_xlabel("time (hours)")
       ax2.set_ylabel("altitude - radius Earth (km)")
       ax2.set_title("AlTITUDE OVER ORBIT DURATION")
'''