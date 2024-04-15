#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello python")


# In[13]:


import pandas as pd
df=pd.read_csv('C:/Users/ivan/Desktop/FL_insurance_sample1.csv',sep=',',nrows=10)


# In[14]:


df.head(10)


# In[15]:


import pandas as pd
import numpy as np


# In[17]:


data=np.random.randint(1,10,(5,3))
df=pd.DataFrame(data, columns=list('ABC'))
df


# In[18]:


# file name for csv
df.to_csv("spam.csv")


# In[19]:


df_load=pd.read_csv("spam.csv")


# In[20]:


df_load


# In[21]:


# check common "?"
get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[22]:


df_load=pd.read_csv("spam.csv", index_col=0)


# In[23]:


df_load


# In[27]:


# youtube

http://u.camdemy.com/media/433


# In[ ]:





# In[ ]:




