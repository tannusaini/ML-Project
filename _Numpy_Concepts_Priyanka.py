#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[6]:


x = np.array([[1,2,3],[4,5,6]])
print(x)


# In[7]:


x.ndim


# In[8]:


x.shape


# In[14]:


x1 = np.array([[7,8,9,10,11],[1,2,3,4,5],[1,2,3,8,4]])


# In[15]:


x1.ndim


# In[16]:


x1.shape


# In[17]:


x1


# In[18]:


x1[0,0]


# In[19]:


x1[1,2]


# In[25]:


x2 = np.random.random((100,100))


# In[26]:


x2[45,52]


# In[27]:


x2[45,:]


# In[28]:


x1[::-1]


# In[29]:


x1[-1::]


# In[30]:


x[::-1]


# In[31]:


x2.flags


# In[32]:


c_array = np.random.rand(1000,1000)


# In[33]:


f_array = np.asfortranarray(c_array)


# In[34]:


c_array.flags


# In[35]:


f_array.flags


# In[37]:


def sum_row(x):
    return np.sum(x[0,:])


# In[38]:


sum_row(x)


# In[39]:


def sum_column(x):
    return np.sum(x[:,0])


# In[40]:


sum_column(x)


# In[41]:


get_ipython().run_line_magic('timeit', 'sum_row(c_array)')


# In[42]:


get_ipython().run_line_magic('timeit', 'sum_row(f_array)')


# In[43]:


get_ipython().run_line_magic('timeit', 'sum_column(c_array)')


# In[45]:


get_ipython().run_line_magic('timeit', 'sum_column(f_array)')


# In[46]:


x4 = np.random.rand(100,10)


# In[47]:


y = x4[:5,:]


# In[49]:


np.may_share_memory(x4,y)


# In[50]:


y [:]=0


# In[51]:


print(x4[:5,:])


# In[53]:


print (y)


# In[55]:


y=np.empty([5,10])


# In[57]:


y[:]=x4[:5,:]


# In[58]:


np.may_share_memory(x4,y)


# In[ ]:


#Creating Arrays From List


# In[59]:


a = range(5)


# In[61]:


b = np.array(a)


# In[62]:


x = np.arange(5)


# In[ ]:


#Creating Random Arrays


# In[63]:


x=np.random.rand(3,3,3)


# In[64]:


x


# In[65]:


print(x.shape)


# In[66]:


shape_tuple = (2,3,4)


# In[67]:


y = np.random.random(shape_tuple)


# In[70]:


print (y.shape)


# In[ ]:





# In[69]:


LOW, HIGH = 1, 11 

SIZE = 10 

x = np.random.randint(LOW, HIGH, size=SIZE) 

print(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




