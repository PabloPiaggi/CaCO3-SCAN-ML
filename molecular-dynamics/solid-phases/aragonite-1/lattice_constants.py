import numpy as np
data=np.genfromtxt("thermo.txt")
a=np.mean(data[100:,:],axis=0)[1]/4
b=np.mean(data[100:,:],axis=0)[2]/4
c=np.mean(data[100:,:],axis=0)[3]/4
print("Average a is ", a)
print("Average b is ", b)
print("Average c is ", c)

