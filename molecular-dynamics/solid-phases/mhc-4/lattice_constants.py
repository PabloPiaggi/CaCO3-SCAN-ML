import numpy as np
data=np.genfromtxt("thermo.txt")
a=np.mean(data[100:,:],axis=0)[1]/2
b=np.mean(data[100:,:],axis=0)[2]/2
c=np.mean(data[100:,:],axis=0)[3]/3
print("Average a is ", a)
print("Average b is ", b)
print("Average c is ", c)

