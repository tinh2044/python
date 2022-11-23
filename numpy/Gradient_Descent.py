import numpy as np
import matplotlib.pyplot as plt
arr = []
data = np.array(arr)
y = data[:,-1]
x = np.zeros((np.size(y),np.size(data, 1)))
x[:,0] = 1
x[:,1:] = data[:, :-1]
def h_func(x,theta):
    return x@theta

def j_func(x,y,theta):
    
    return (1/(2*m))*np.transpose(h_func(x,theta) - y)*np.transpose(h_func(x,theta) - y)

def gradient_descent(x,y,step, iter):
    theta = zeros(np.size(x,1))
    j_list = np.zeros((iter,2))
    m = np.size(y)
    x_transpose = np.transpose(x)
    prev_cost = j_func(x,y, theta)
    for i in range(iter):
        error = h_func(x, theta) - y
        
        theta -= (step/m)*(x_transpose*error)
        
        const = j_func(x, y, theta)
        
        if np.round(const,15) == np.round(prev_cost, 15):
            print('Reach optima at I = %d ; J = %.6f'%(i,cost))
            j_list[:,0] = range(i,iter)
            j_list[:,1] = const
            break
        j_list[i,0] = i
        j_list[i,1] = const
        yield theta
        yield j_list
        
        
    