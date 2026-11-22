import numpy as np

#-----Example data------#
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

learning_rate = 0.01


#-----1. Linear model------#
def model(x, m):
    return m * x


#-----2. Error function (Mean Squared Error)------#
def error_function(m):
    predictions = model(x, m)
    return np.mean((predictions - y) ** 2)


#-----3. Derivative of the error function------#
def derivative(m):
    predictions = model(x, m)
    return np.mean(2 * x * (predictions - y))


#-----4. Gradient descent update step------#
def update_step(m):
    return m - learning_rate * derivative(m)