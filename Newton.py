import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

w1 = sp.Symbol('w1')
w2 = sp.Symbol('w2')
g = sp.log(1 + sp.exp(w1 ** 2 + w2 ** 2))  #function we are minimizing
g_f = sp.lambdify((w1, w2,), sp.log(1 + sp.exp(w1 ** 2 + w2 ** 2)))

grad = ([sp.diff(g, w1), sp.diff(g, w2)]) #finding the gradient
grad_lambda = sp.lambdify((w1, w2), grad)


def grad_f(w1, w2): # converting the gradient into a function that gives and array output
    return np.asarray(grad_lambda(w1, w2))


hess = [[sp.diff(grad[0], w1), sp.diff(grad[0], w2)], [sp.diff(grad[1], w1), sp.diff(grad[1], w2)]] #finding the hessian
hess_lambda = sp.lambdify((w1, w2), hess)


def hess_f(w1, w2): # converting the hessian into a function that gives and array output
    return np.asarray(hess_lambda(w1, w2))

#Initial point
w_0 = [1, 1] # if initial point is [4,4], we can see the algorithm converges faster due to properties of g
x_axis = [w_0[0]]
y_axis = [w_0[1]]
z_axis = [g_f(w_0[0], w_0[1])]

#Newton's method
w_prev = w_0
for _ in range(0, 10):
    w_prev = w_prev - np.linalg.inv(hess_f(w_prev[0], w_prev[1])) @ grad_f(w_prev[0], w_prev[1])
    x_axis.append(w_prev[0])
    y_axis.append(w_prev[1])
    z_axis.append(g_f(w_prev[0], w_prev[1]))
    if w_prev[0]==0 and w_prev[1]==0: #check how fast it has converged to minimum (we know the minimum in this case)
        print(f"Minimum reached after {_+1} steps")
        break

#Plotting
ax = plt.axes(projection='3d')
ax.plot3D(x_axis, y_axis, z_axis)
ax.scatter3D(w_0[0],w_0[1],g_f(w_0[0], w_0[1]), color='green')
ax.scatter3D(w_prev[0],w_prev[1],g_f(w_prev[0], w_prev[1]), color='red')
plt.show()
