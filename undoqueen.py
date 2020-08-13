#!/usr/bin/env python
# coding: utf-8

# In[2]:


def undoqueen(i,j,board):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][i]=0
    board['nwtose'][j-i]=0
    board['swtone'][j+i]=0

