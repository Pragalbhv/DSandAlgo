#!/usr/bin/env python
# coding: utf-8

# In[5]:


def isfree(i,j,board):
    return(not(board['row'][i]or board['col'][j] or board['nwtose'][j-1] or board['swtone'][j+i]))

