#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[ ]:


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
    

random_number = random_randint(0, top_of_range)

