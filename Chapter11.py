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

def x_y(typ, cvv, vpp):
    lyst = []
    for j,i in enumerate(cvv):
        lyst.append([])
        for k in i:
            if typ =='x':
                lyst[j].append(vpp[k][0])
            else:
                lyst[j].append(vpp[k][1])
    return tuple(lyst)

x = x_y('x', cvv, vpp)
y = x_y('y', cvv, vpp)
#%%
import numpy
def area(x,y):
    a = len(x) * [0]
    for i in range(len(x)):
        for j in range(len(x[i])):
            a[i] += x[i][j] * y[i][j-1] - x[i][j-1] * y[i][j]
        a[i] = a[i]/2
    return numpy.array(a)


areaa = area(x,y)      
        
#%%
def centroid(x,y, areaa):
    xcent = len(x) * [0]
    ycent = len(y) * [0]
    for i in range(len(y)):
        for j in range(len(y[i])):
            xcent[i]  +=  ((x[i][j] + x[i][j-1]) * (x[i][j]*y[i][j-1]-x[i][j-1]*y[i][j])) / (6* areaa[i])
            ycent[i] += ((y[i][j] + y[i][j-1]) * (x[i][j]*y[i][j-1]-x[i][j-1]*y[i][j])) / (6* areaa[i])
    return numpy.array(xcent), numpy.array(ycent)

cx, cy = centroid(x,y,areaa)

def distance_center(xcenter, ycenter):
    dist_cent=(xcenter**2 + ycenter**2)**0.5
    return dist_cent


distcent = distance_center(cx, cy)       
        
#%%
from scipy import stats as s
from numpy import polyfit as p

def t_test(areaa, distcent):
    maxxy = max(distcent)
    t_value, p_value = s.ttest_ind(areaa[distcent<=maxxy/2], areaa[distcent>maxxy/2])
    return t_value, p_value


t_value, p_value = t_test(areaa, distcent)


def linear_fit(areaa, distcent):
    slope, y_intercept = p(distcent, areaa,1)
    return slope, y_intercept


slope, y_intercept = linear_fit(areaa, distcent)

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
    
#function to draw the wing disc
def draw_disc(cpx, cpy, area, size):
    #input arguments: 
    ## cpx, cpy: x,y/positions of the vertices of all cells 
	# format: list (1 element per cell) of sublists (1 number per vertex, eg 3 numbers for a triangle). 
    ## area: cell area
	# format: 1-dimentsional numpy array (1 number per cell)
    ## size: 'large' for the large disc and 'small' for the small disc
    
    polygs = []
    for i in range(len(cpx)):
    	polyg = []
    	for j in range(len(cpx[i])):
    		polyg.append([cpx[i][j], cpy[i][j]])
    	polygs.append(Polygon(polyg))
    patches = PatchCollection(polygs)
    patches.set_cmap('jet')
    colors = 1 * area
    colors[colors>14] = 14 # color value for all the mitotic cells (area>14) is set to 14
    patches.set_array(np.array(colors)) #for colors

    fig = plt.figure()
    panel = fig.add_subplot(1,1,1)
    panel.add_collection(patches)
    color_bar = fig.colorbar(patches)
    color_bar.set_label('Cell area (um2)', rotation = 270, labelpad = 15)
    panel.set_xlim(-120, 110)
    panel.set_ylim(-85, 85)
    panel.set_aspect('equal')
    plt.title(size+' wing disc')


        
draw_disc(x, y, areaa, 'large')


#%% small disc

cv_small = cv('cv_small.txt')
vp_small = vp('vp_small.txt')

x_small = x_y('x', cv_small, vp_small)
y_small = x_y('y', cv_small, vp_small)

area_small = area(x_small, y_small)

xcenter_small, ycenter_small = centroid(x_small, y_small, area_small)

distance_center_small = distance_center(xcenter_small, ycenter_small)

t_value_small, p_value_small = t_test(area_small, distance_center_small)

slope_small, y_intercept_small = linear_fit(area_small, distance_center_small)

draw_disc(x_small, y_small, area_small, 'small')


        