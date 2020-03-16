import numpy as np

#2
x=[1,2,3]
y=np.array(x)
print(y)

#3
x=np.array([[2,3,4], [5,6,7], [8,9,10]])
print(x)

#4
x=np.zeros(10)
x[6]=11
print(x)

#5
x=np.array([1,2,3])
x=x[::-1]
print(x)

#6
x=np.array([1,2,3])
print(x.dtype)
x=x.astype(float)
print(x.dtype)

#7
x=np.zeros((8,8), dtype=np.int)
x[1::2,::2]=1
x[::2, 1::2]=1
print(x)
