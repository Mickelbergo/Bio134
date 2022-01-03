# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:06:16 2021

@author: copet
"""

def cv(file):
    lyst = []
    with open(file) as f:
        for i in f.readlines():
            line =i.split()
            line=[int(i) for i in line]
            lyst.append(tuple(line))
    return tuple(lyst)

print(cv('cv.txt'))

def vp(file):
    lyst=[]
    with open(file) as f:
        for i in f.readlines():
            line= i.split()
            line=[float(i) for i in line]
            lyst.append(tuple(line))
    return tuple(lyst)
vpp = vp('vp.txt')
cvv = cv('cv.txt')

#%%

def x_y(typ):
    lyst = []
    for j,i in enumerate(cvv):
        lyst.append([])
        for k in i:
            if typ =='x':
                lyst[j].append(vpp[k][0])
            else:
                lyst[j].append(vpp[k][1])
    return tuple(lyst)

x = x_y('x')
y = x_y('y')
#%%
import numpy
def area(x,y):
    a = len(x) * [0]
    for i in range(len(x)):
        for j in range(len(x[i])):
            a[i] += x[i][j] * y[i][j-1] - x[i][j-1] * y[i][j]
        a[i] = a[i]/2
    return numpy.array(a)

print(area(x,y)[-1])

areaa = area(x,y)      
        
#%%
def centroid(x,y, area):
    xcent = len(x) * [0]
    ycent = len(y) * [0]
    for i in range(len(y)):
        for j in range(len(y[i])):
            xcent[i]  +=  ((x[i][j] + x[i][j-1]) * (x[i][j]*y[i][j-1]-x[i][j-1]*y[i][j])) / (6* area[i])
            ycent[i] += ((y[i][j] + y[i][j-1]) * (x[i][j]*y[i][j-1]-x[i][j-1]*y[i][j])) / (6* area[i])
    return numpy.array(xcent), numpy.array(ycent)

cx, cy = centroid(x,y,areaa)
print(cx[1])
print(cy[1])

def distance_center(xcenter, ycenter):
    dist_cent=(xcenter**2 + ycenter**2)**0.5
    return dist_cent

print(distance_center(cx, cy)[1])
        
        
        
        
        
        
        
        
        