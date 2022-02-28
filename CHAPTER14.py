# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:19:32 2021

@author: copet
"""

#revision

#slicing
import numpy as np

def La(prot):
    N = len(prot)
    dprot = np.zeros(N)
    dprot[1:-1] += -2 * prot[1:-1] + prot[:-2] + prot[2:]
    dprot[0] = -prot[0] + prot[1]
    dprot[-1] = -prot[-1] + prot[-2]
    return dprot
    
N = 20
np.random.seed(0)
a = np.zeros(N) + 1 + 0.3 * np.random.rand(N)
print(La(a))


#polygon areas

def calc_areas(vp,cv):
    areas = []
    for i in range(len(cv)):
        area = 0
        for j in range(len(cv[i])):
            v1 = cv[i][j]
            v0 = cv[i][j-1]
            area += 0.5 * (vp[v1][0]*vp[v0][1] - vp[v1][1]*vp[v0][0])
        areas.append(area)
    return (areas)

cv = [[0, 1, 2, 5, 6],[2, 3, 4, 7, 5]] #vertex numbers per cell
vp = [[0.8,5.5],[2.4,7.0],[4.1,6.4],[6.3,7.0],[7.6,4.8],[3.9,4.0],\
     [1.9,3.4],[6.3,3.3]] #x and y positions per vertex

print(calc_areas(vp,cv))






#dilation

im = np.array([[[0.6,0.5,0.7],[0.0,0.3,0.2],[0.7,0.5,0.1]],\
               [[0.4,0.8,0.7],[0.5,0.3,0.2],[0.6,0.5,0.3]],\
               [[0.7,0.7,0.6],[0.8,0.4,0.3],[0.4,0.8,0.3]]])
    
def special_dilation(x):
    for i in range(len(x)):
        for k in range(len(x[i])):
            for m in range(len(x[i][k])):
                try:
                    if x[i][k][m] < x[i][k+1][m]:
                        x[i][k][m] = x[i][k+1][m]
                except:
                    continue
    return x
im_new = special_dilation(im)
print (im_new)
print (np.sum(im_new))


#longest shared sequence

seq1 = 'MNENLFASFIAPTILGLPAAVLIILFPPLLIPTSKYLINNRLITTQQWLIKLTSKQMMTMHNTKGRTWSLMLVSLIIFIATTNLLGLLPHSFTPTTQLSMNLAMAIPLWAGTVIMGFRSKIKNALAHFLPQGTPTPLIPMLVIIETISLLIQPMALAVRLTANITAGHLLMHLIGSATLAMSTINLPSTLIIFTILILLTILEIAVALIQAYVFTLLVSLYLHDNT'

seq2 = 'MMTNLFSVFDPSTTILNLSLNWLSTFLGLLLIPFSFWLLPNRFQVVWNNILLTLHKEFKTLLGPSGHNGSTLMFISLFSLIMFNNFLGLFPYIFTSTSHLTLTLALAFPLWLSFMLYGWINHTQHMFAHLVPQGTPPVLMPFMVCIETISNVIRPGTLAVRLTANMIAGHLLLTLLGNTGPMTTNYIILSLILTTQIALLVLESAVAIIQSYVFAVLSTLYSSEVN'


if len(seq1) < len(seq2):
    short = seq1
    long = seq2

else:
    long = seq1
    short = seq2
    
for i in range(len(short)):
    for j in range(len(long)):
        if short[i:-j] in long:
            print(short[i:j-1])
            
            
class dog:
    
    
    def __init__(self):
        pass
    
            