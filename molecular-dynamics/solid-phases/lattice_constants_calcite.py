import numpy as np
folders=np.array(["calcite-1","calcite-2","calcite-3","calcite-4"])

a = []
c = []
for folder in folders:
    data=np.genfromtxt(folder + "/thermo.txt")
    a.append( (np.mean(data[100:,:],axis=0)[1]/6+np.mean(data[100:,:],axis=0)[2]/6)/2.0 )
    c.append(np.mean(data[100:,:],axis=0)[3]/2)
a = np.array(a)
c = np.array(c)
print(a,c)
print("Average a is ", np.mean(a), " +- ", np.std(a))
print("Average c is ", np.mean(c), " +- ", np.std(c))

