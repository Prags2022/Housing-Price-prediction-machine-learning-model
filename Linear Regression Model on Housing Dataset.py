#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from  sklearn import linear_model
from sklearn.model_selection import train_test_split


# In[33]:


data=pd.read_csv("Housing.csv")
data


# In[34]:


x=np.array(data['price'])
y=np.array(data['area'])
x.shape


# In[35]:


y.shape


# In[36]:


x=x.reshape(len(x),1)
y=y.reshape(len(y),1)


# In[48]:


x_train=x[:-250]
x_test=x[-250:]
y_train=y[:-250]
y_test=y[-250:]


# In[49]:


plt.scatter(x_test,y_test,color="red")
plt.title("Pandas data")
plt.xlabel('price')
plt.ylabel('area')
plt.show()


# In[50]:


#Creating Regression model
x_train.shape
y_train.shape


# In[53]:


reg= linear_model.LinearRegression()
reg.fit(x_train,y_train)
plt.plot(x_test,reg.predict(x_test),color='red',linewidth=3) 
plt.scatter(x_test,y_test,color="blue")
plt.title('test_data')
plt.xlabel('price')
plt.ylabel('area')
plt.show()


# In[57]:


X_train, X_test, Y_train, Y_test = train_test_split(x,y , test_size = 0.2, random_state = 0)
X_test.shape


# In[60]:


reg= linear_model.LinearRegression()
reg.fit(X_train,Y_train)
plt.plot(X_test,reg.predict(X_test),color='red',linewidth=0.5) 
plt.scatter(X_test,Y_test,color="blue")
plt.title('test_data')
plt.xlabel('price')
plt.ylabel('area')
plt.show()


# In[ ]:




