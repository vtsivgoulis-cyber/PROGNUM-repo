#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Sirius data
apparentMagnitude = float(input("enter apparentMagnitude: "))
absoluteMagnitude = float(input("enter absoluteMagnitude: "))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
d_ly = d * 3.26164
print(f"The distance in parsecs is {d} and in lightyears {d_ly}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




