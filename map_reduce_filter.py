#!/usr/bin/env python
# coding: utf-8

# In[1]:


list_1 = ['sachin','dravid','virat',]


# In[4]:


list_2 = map(str.upper,list_1)


# In[7]:


print(list(list_2))


# In[ ]:





# In[8]:


def lenght(x):
    return len(list(x))


# In[13]:


list_3 = map(lenght,list_1)


# In[14]:


print(list(list_3))


# In[ ]:





# In[17]:


list_4 = ['sachin','dravid','kohli']


# In[21]:


def a_in_list(x):
    return 'a' not in x


# In[22]:


list_5 = filter(a_in_list,list_4)


# In[23]:


print(list(list_5))


# In[ ]:





# In[ ]:





# In[24]:


from functools import reduce


# In[31]:


list_6 = reduce(lambda x,y: x + " plays after " + y, list_4)


# In[32]:


print(list_6)


# In[35]:


list_1=["sachin","dravid","virat"]
from functools import reduce
list_6 = reduce(lambda x,y : x + " plays after " +y,list_1)
print (list_6)


# In[ ]:





# In[ ]:





# In[ ]:





# In[38]:


a = 0
empty_list = []
while a < 5: a = a + 1; empty_list.append(a)


# In[39]:


empty_list


# In[ ]:




