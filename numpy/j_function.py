import numpy as np

a= [[1,2,3,4,5,6,],[7,8,9,10,11,12]]
theta= [6,7,5,3,2,1,4]
_a = np.array(a)
_b = _a[:,-1]
_c = np.zeros((np.size(_b), np.size(_a,1)))
_c[:,0] = 1
_c[:,1:] = _a[:,:-1]
print(_c)
m = np.size(_b)
def theta(X, Theta):
    return X@Theta

def computeCost(X, y , theta): 
    predict = theta(X, theta)
    
    sqrError = (predict - y)**2
    
    j = (1/(2*m))*np.sum(sqrError)
    
    return j
def computeCostVec():
    return (1/(2*m))*np.transpose(theta(X, Theta) - y)*(theta(X, Theta) - y)
print(m)