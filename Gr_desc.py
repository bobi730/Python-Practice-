import numpy as np
from matplotlib import pyplot as plt

g = lambda w: w @ np.transpose(w) #function to minimize
grad = lambda w: np.multiply(np.transpose(w),2) #gradient

w_0=[10 for x in range(0,10)] #initial point

def descent(alpha): #function of the step-length alpha
    w_prev=w_0
    xaxis=[0] #iteration axis
    yaxis=[g(w_0)]
    for k in range(1,100):
        w_k=w_prev-alpha*grad(w_prev)
        w_prev=w_k
        xaxis.append(k)
        yaxis.append(g(w_k))
    return (xaxis,yaxis)

#Plotting for three different steplengths
points1=descent(0.001)
points2=descent(0.1)
points3=descent(1.001)
plt.plot(points1[0], points1[1])
plt.plot(points2[0], points2[1])
plt.plot(points3[0], points3[1])
plt.show()