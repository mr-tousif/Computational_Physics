#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#the first argument in any method can be anything in place of self. we may use self is a dummy variable

class five:
    '''this is even better class'''
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(arg):
        '''addition'''
        z=arg.x+arg.y
        return z
    def rms(par):
        '''square root of x and y'''
        import math
        d=math.sqrt(par.x**2+par.y**2)
        return d

