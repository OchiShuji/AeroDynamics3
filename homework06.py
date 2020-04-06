import numpy as np 
from matplotlib import pyplot as plt 

gamma = 1.4
t_f = np.linspace(0.5,1.5,100)
t_r = np.linspace(0.5,1.5,1000000)
s_f = np.log(np.power(t_f,1/(gamma-1))*np.sqrt(((gamma+1)-2*t_f)/(gamma-1)))



       

s_r_m = gamma/(gamma-1)*np.log(t_r)-np.log(((1+gamma)/2)-np.sqrt(np.power((1+gamma)/2,2)-gamma*t_r))
s_r_p = gamma/(gamma-1)*np.log(t_r)-np.log(((1+gamma)/2)+np.sqrt(np.power((1+gamma)/2,2)-gamma*t_r))

plt.plot(s_f,t_f,label="Fanno")
plt.plot(s_r_m,t_r,label="Rayleigh")
plt.plot(s_r_p,t_r,label="Rayleigh")

plt.legend(loc="upper right")
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2/3))
ax.xaxis.set_tick_params(which="both",direction="in")
ax.yaxis.set_tick_params(which="both",direction="in")
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

plt.title("Fanno & Rayleigh Diagram "+r"($\gamma=1.4$)")
plt.xlim(-1.0,0.0)
plt.xticks([-1.0,-.8,-.6,-.4,-.2,0.0],["-1.0","-0.8","-0.6","-0.4","-0.2","0.0"])
plt.yticks([0.0,0.5,1.0,1.5,2.0],["0.0","0.5","1.0","1.5","2.0"])
plt.xlabel(r"$\frac{s-s^*}{R}$",fontsize="16")
plt.ylabel(r"$\frac{T}{T^*}$",fontsize="16")
plt.show()