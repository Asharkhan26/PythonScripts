# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:47:18 2021

@author: Ashar
"""

import math
# consider sides as a,b,c where a and b are adjacent sides

a = 10
b = 5
#calculating Hypotaneus
c = math.sqrt(a**2 + b**2)
print(c)
#calculating area of triangle
area = (a*b)/2
area = math.floor(area)
print(area)
