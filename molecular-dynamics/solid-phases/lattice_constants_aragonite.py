import numpy as np
folders=np.array(["aragonite-1","aragonite-2","aragonite-3","aragonite-4"])
a = []
b = []
c = []
for folder in folders:
    data=np.genfromtxt(folder + "/thermo.txt")
    a.append(np.mean(data[100:,:],axis=0)[1]/4)
    b.append(np.mean(data[100:,:],axis=0)[2]/4)
    c.append(np.mean(data[100:,:],axis=0)[3]/4)
a = np.array(a)
b = np.array(b)
c = np.array(c)
print(a,b,c)
print("Average a is ", np.mean(a), " +- ", np.std(a))
print("Average b is ", np.mean(b), " +- ", np.std(b))
print("Average c is ", np.mean(c), " +- ", np.std(c))

