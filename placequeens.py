#!/usr/bin/env python
# coding: utf-8

# In[3]:


def placequeens(i,board):
    n=len(board)
    for j in n:
        if isfree(i,j,board):
            addqueen(i,j,board)
            if i==n-1:
                return(true)
            else:
                extendsol=placequeen(i+1,board)
            if extedsol:
                return(True)
            else:
                undoqueen(i,j,bioard)
        else:
            rteurn(False)

