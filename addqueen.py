#!/usr/bin/env python
# coding: utf-8

# In[1]:


def addqueen(i,j,board):
    board['queen'][i]=j
    board['row'][i]=1
    board['col'][i]=1
    board['nwtose'][j-i]=1
    board['swtone'][j+i]=1

