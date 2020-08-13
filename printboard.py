#!/usr/bin/env python
# coding: utf-8

# In[10]:


def printboard(board):
    for row in sorted(board['queen'].keys()):
        print(row,board['queen'][row])


# In[12]:


def printbeauty(board):
    import numpy as np
    A=[[0]*M]*N
    for row in sorted(board['queen'].keys()):
        A[row][board['queen'][row]]=1;
    print(np.matrix(A))

