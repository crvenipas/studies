#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np

lst = [int(i) for i in input().split()]
x = int(input())

if x in lst:
    np_lst = np.array(lst)
    x_index = np.where(np_lst==x)
    print(' '.join(map(str,x_index)))
else:
    print('Отсутствует')


# In[ ]:




