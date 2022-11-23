import matplotlib.pyplot as plt
import numpy as np
x = np.loadtxt('univariate.txt', delimiter=',')
Theta = np.loadtxt('univariate_theta.txt', delimiter=',')
y = np.copy(x[:,-1])
x[:,1] = x[:,0]
x[:,0] = 1
predict = x@Theta
predict *= 10000
print('%d nguoi: %.2f' %(x[0,1]*10000,predict[0]))

np.savetxt('predict_value.txt', predict, fmt='%.6f')
plt.plot(x[:,1:], y ,'rx')
plt.plot(predict/1000, y ,'-b')
plt.show()