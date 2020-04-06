import numpy as np 
from matplotlib import pyplot as plt 

beta = np.linspace(0.001,np.pi/2,100)
M1 = [1.2,1.6,2.0,3.0,10.0,10000.0]
gamma = 1.4
rad2deg = 180 / np.pi

def theta(beta,M):
    tan_theta = 2*(M*M*np.sin(beta)*np.sin(beta)-1)/np.tan(beta)/(M*M*(gamma+np.cos(2*beta))+2)
    return np.arctan(tan_theta)

for M in M1:
    theta_1 = theta(beta,M)
    label = r"$M_1=$" + str(M)
    plt.plot(beta*rad2deg,theta_1*rad2deg,label=label)
    plt.legend()

M1s = np.linspace(0.001,100,10000)
beta_s = np.arcsin(np.sqrt(1/gamma/M1s/M1s*((gamma+1)*M1s*M1s/4-(3-gamma)/4+np.sqrt((gamma+1)*((9+gamma)/16-(3-gamma)*M1s*M1s/8+(gamma+1)/16*M1s*M1s*M1s*M1s)))))
theta_s = theta(beta_s,M1s)
beta_m = np.arcsin(np.sqrt(1/gamma/M1s/M1s*((gamma+1)*M1s*M1s/4-1+np.sqrt((gamma+1)*(1+(gamma-1)*M1s*M1s/2+(gamma+1)*M1s*M1s*M1s*M1s/16)))))
theta_m = theta(beta_m,M1s)
plt.plot(beta_s*rad2deg,theta_s*rad2deg,color="grey")
plt.plot(beta_m*rad2deg,theta_m*rad2deg,color="grey")
plt.annotate(r"$M_2=1$",xy=(63,30),xycoords='data',xytext=(-70, 10),textcoords='offset points',fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r"$\theta=\theta_{max}$",xy=(65,30),xycoords='data',xytext=(70, 30),textcoords='offset points',fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.xlabel(r"$\beta$")
plt.ylabel(r"$\theta$")
plt.xlim(0,90)
//plt.ylim(0,50)
plt.show()


   
