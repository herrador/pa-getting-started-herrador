#!/usr/bin/env python
# coding: utf-8

# In[ ]:


NAME = "Andrew Herrador"
# University of Arizona email address
EMAIL = "herrador@email.arizona.edu"
# Names of any collaborators.  Write N/A if none.
COLLABORATORS = "N/A"


# In[ ]:


Andrew Herrador


# In[3]:


def multiply(a: int, b: int) -> int:
    """
    Takes two ints and returns their product
    """
    # YOUR CODE HERE
    return a*b


# In[4]:


assert multiply(2,2) == 4
assert multiply(2,0) == 0


# In[7]:


def weird_request(seq):
    """
    takes a list of strings, reverses them, drops the element at the front, and returns what remains.
    """
    # YOUR CODE HERE
    seq.reverse()
    return seq[1:]


# In[8]:


assert weird_request([1,2,3]) == [2,1]
assert weird_request([1]) == []


# In[ ]:




