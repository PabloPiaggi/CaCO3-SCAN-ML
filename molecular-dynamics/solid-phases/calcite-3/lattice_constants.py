import numpy as np
data=np.genfromtxt("thermo.txt")
a=np.mean(data[100:,:],axis=0)[1]/6
b=np.mean(data[100:,:],axis=0)[2]/6
c=np.mean(data[100:,:],axis=0)[3]/2
print("Average a is ", (a+b)/2.)
print("Average c is ", c)

