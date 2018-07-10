from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
values = list(map(int,input().strip().split(' '))) 
labels = np.zeros(shape=(values[1]))
x_train = np.zeros(shape=(values[1],values[0]))
#print(values[1]);
#print(range(0,values[1]))
for i in range(0,values[1]):
    #print(i)
    v = list(map(float,input().strip().split(' ')))
    #print(v)
    x_train[i,:] = v[0:len(v)-1]
    labels[i] = v[len(v)-1];
# Create linear regression
regr = LinearRegression()

# Fit the linear regression
model = regr.fit(x_train, labels)
#print(feature)
n = int(input());
x_test = np.zeros(shape=(n,values[0]))
for i in range(0,n):
	v = list(map(float,input().strip().split(' ')))
	x_test[i,:] = v[0:len(v)]
y_predict = regr.predict(x_test)
for i in y_predict:
    print(i)

