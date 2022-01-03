# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:56:42 2021

@author: copet
"""

#exercise binning data

import numpy as np
a = np.array([0.13,0.4,0.52])
a = np.array([0.3,0.2,0.4,0.1,0.5,0.5,0.7,1.0,0.3,0.3,0.2,0.1,\
      0.8,0.8,0.7,0.6,0.3,0.0,0.1,0.2,0.7,0.4])**2
    
a = a * 5
a = a.astype(int)
print(np.bincount(a))

#2

sex = np.array([0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]) # male: 0; female: 1
height = np.array([1.83, 1.72, 1.61, 1.68, 1.79, 1.75, 1.92, 1.76, 1.66, 1.68, 1.69, 1.61, 1.70, 1.78]) # in meters

print(np.bincount(sex, height))
print(np.bincount(sex))

heights = np.bincount(sex,height)
sexes = np.bincount(sex)
ratio = heights/sexes

print(ratio[0]-ratio[1])


