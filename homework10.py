import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize
from tqdm import tqdm

n = 10000
gamma = 1.4
ome_i = np.linspace(0.1,np.pi/2,n)
beta_i = ome_i
M1 = np.zeros(n)
theta_i = np.zeros(n)
M2 = np.zeros(n)
theta_r = np.zeros(n)
zeta = np.zeros(n)
beta_r = np.zeros(n)
ome_r = np.zeros(n)

xi = [0,0.4,0.6,0.8,0.9,1.0]   #p2/p1 i.e. M1
for x in tqdm(xi):
    for i in range(0,n-1):
        M1[i] = np.sqrt((x*(gamma+1) + gamma - 1)/2/gamma/np.sin(beta_i[i])/np.sin(beta_i[i]))
        theta_i[i] = np.arctan((x-1)/(1+gamma*M1[i]*M1[i]-x)*np.sqrt(((2*gamma*M1[i]*M1[i]-gamma+1)/(gamma+1)-x)/(x+(gamma-1)/(gamma+1))))
        M2[i] = ((gamma-1)*M1[i]*M1[i]*np.sin(beta_i[i])*np.sin(beta_i[i])+2)/(2*gamma*M1[i]*M1[i]*np.sin(beta_i[i])*np.sin(beta_i[i])+gamma-1)/np.sin(beta_i[i]-theta_i[i])/np.sin(beta_i[i]-theta_i[i])
        theta_r[i] = - theta_i[i]
        def f(zeta):
            return (zeta-1)/(1+gamma*M2[i]*M2[i]-zeta)*np.sqrt(((2*gamma*M2[i]*M2[i]-gamma+1)/(gamma+1)-zeta)/(zeta+(gamma-1)/(gamma+1))) - np.tan(theta_r[i])
        zeta[i] = optimize.fsolve(f,0)
        beta_r[i] = np.arcsin(np.sqrt((zeta[i]*(gamma+1)+gamma-1)/2/gamma/M2[i]/M2[i]))
        ome_r[i] = beta_r[i] - theta_r[i]
    plt.plot(ome_i,ome_r,label=str(x))


plt.legend()
plt.show()

    