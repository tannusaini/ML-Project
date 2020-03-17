#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#Views and Copies

#Views
x=np.random.rand(100,10)
y=x[:5, :]
print(np.may_share_memory(x,y))

y[:]=0
print(x[:5, :])


# In[2]:


#Copies
x=np.random.rand(100,10)
y=np.empty([5,10])
y[:]=x[:5, :]
print(np.may_share_memory(x,y))

y[:]=0
print(x[:5, :])


# In[3]:


#Random arrays
x=np.random.rand(2, 2, 2)
print(x.shape)

shape_tuple=(2, 3, 4)
y=np.random.random(shape_tuple)
print(y.shape)

#rantint func
LOW, HIGH=1, 11
SIZE=10
x=np.random.randint(LOW, HIGH, size=SIZE)
print(x)


# In[4]:


#data types
x=np.random.random((10,10))
print(x.dtype)

x=np.array(range(10))
print(x.dtype)

x=np.array(['hello','world'])
print(x.dtype)

x=np.ones((10,10), dtype=np.int)
print(x.dtype)


# In[5]:


#Vectorized operations
x=np.array([1,2,3,4])
print(x+1)

y=np.array([-1,2,3,0])
print(x*y)

#Matrix multiplication
print(np.dot(x,y))

#Comparison
print(x==y)


# In[6]:


#Universal func

#square func
x=np.arange(5,10)
print(np.square(x))

#mod func
y=np.ones(5)*10
print(np.mod(y,x))

#minimum and min func
print(np.minimum(x,7))
print(np.min(x))

#repeat func
z=np.repeat(x, 3).reshape(5,3)
print(z)

#median func
print(np.median(z))
print(np.median(z, axis=0))
print(np.median(z, axis=1))

#accumulate func
print(np.add.accumulate(x))

#multiply func
print(np.multiply.outer(x, x))


# In[2]:


#Broadcasting rules
x=np.array([[0,0,0], [10,10,10], [20,20,20]])
y=np.array([1,2,3])
print(x+y)

#Reshaping
x=np.arange(24)
x.shape=2, 3, -1
print(x)

#Vector stacking
x=np.arange(0, 10, 2)
y=np.arange(0, -5, -1)
print(np.vstack([x, y]))
print(np.hstack([x, y]))
print(np.dstack([x, y]))

#resize
x=np.arange(3)
print(np.resize(x, (8,)))


# In[4]:


#Boolean mask
x=np.array([1,3,-1,5,7,-1])
mask=(x<0)
print(mask)

x[mask]=0
print(x)

x=np.random.random(50)
print((x>.5).sum())


# In[2]:


#Indexing and Slicing
x=np.random.random((100,100))

#Indexing
y=x[42,87]
print(y)

#Slicing
#printing the entire row
print(x[1,:])

#printing the entire column
print(x[:,1])

#Reversing array
print(x[::-1])


# In[3]:


#Numpy assignment

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

