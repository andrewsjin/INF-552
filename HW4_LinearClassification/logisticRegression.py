import sys 
import numpy as np


filename = sys.argv[1]
data = np.loadtxt(filename, dtype = "float", delimiter = ",")
X = data[:,0:3]
Y = data[:,4]
Y = Y[:, np.newaxis]
m, n = np.shape(X)
ones = np.ones((m,1))
X = np.concatenate((ones, X), axis = 1)

weights = np.random.rand(1,n+1)
for i in range(7000):
	yxwT = np.multiply(np.dot(X, weights.T), Y)
	delta = -1 * np.exp(-yxwT) / (1 + np.exp(-yxwT))
	delta = np.multiply(delta, np.multiply(X, Y))
	delta = np.sum(delta, axis = 0)
	delta = delta / m
	weights -= 0.01 * delta
predict = np.dot(X, weights.T)
res = np.ones((m,1));
res[predict < 0] = -1
res = np.multiply(res, Y)
res[res < 0] = 0
print np.sum(res, axis=0)[0] / float(m)
print weights