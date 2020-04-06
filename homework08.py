import numpy as np 
from matplotlib import pyplot as plt 

gamma = 1.4
M = np.linspace(1,5,1000)

nu = np.sqrt((gamma+1)/(gamma-1))*np.arctan(np.sqrt((gamma-1)*(M*M-1)/(gamma+1)))-np.arctan(np.sqrt(M*M-1))
alp = np.arcsin(1/M)

plt.plot(M,nu*180/np.pi,label=r"$\nu$")
plt.plot(M,alp*180/np.pi,label=r"$\alpha$")
plt.xlabel("Mach Number"+" "+r"$M$")
plt.ylabel(r"$\nu$,$\alpha$ [deg]")
plt.xticks([1,2,3,4,5],["1","2","3","4","5"])
plt.yticks([0,15,30,45,60,75,90],["0","15","30","45","60","75","90"])
plt.xlim(0.9,5.1)
plt.ylim(0,90)
ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_tick_params(which="both",direction="in")
ax.yaxis.set_tick_params(which="both",direction="in")
plt.legend()
plt.show()

M = np.linspace(1,50,10000)

nu = np.sqrt((gamma+1)/(gamma-1))*np.arctan(np.sqrt((gamma-1)*(M*M-1)/(gamma+1)))-np.arctan(np.sqrt(M*M-1))
alp = np.arcsin(1/M)


plt.plot(M,nu*180/np.pi,label=r"$\nu$")
plt.plot(M,alp*180/np.pi,label=r"$\alpha$")
plt.plot(np.linspace(0,51,100),130.5*np.linspace(1,1,100),linewidth=0.5, linestyle="--",color="black")
plt.xlabel("Mach Number"+" "+r"$M$")
plt.ylabel(r"$\nu$,$\alpha$ [deg]")
plt.xticks([0,10,20,30,40,50],["0","10","20","30","40","50"])
plt.yticks([0,20,40,60,80,100,120,130.5,140],["0","20","40","60","80","100","120","130.5","140"])
plt.xlim(0,51)
plt.ylim(0,140)
ax = plt.gca()
ax.xaxis.set_minor_locator(plt.MultipleLocator(2))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5))
ax.xaxis.set_tick_params(which="both",direction="in")
ax.yaxis.set_tick_params(which="both",direction="in")
plt.legend()
plt.show()