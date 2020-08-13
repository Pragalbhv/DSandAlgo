#!/usr/bin/env python
# coding: utf-8

# In[1]:


from initialize import *
from isfree import *
from addqueen import *
from undoqueen import *
from addqueen import *
from printboard import *
from placequeens import *


# In[2]:


def nQueens():
    n=int(input("enter no of Queens"))
    board={}
    initialize(board,n)
    if placequeens(0,board):
        printboard(board)
    return(True)

