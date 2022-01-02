# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:41:33 2022

@author: copet
"""

numbers = [5, -2, -3, 0, 4, 1, -7, 0, 8]

def xy(lyst):
    lyst1 = []
    lyst2 = []
    for i in lyst:
        if i > 0:
            lyst1.append(i)
        elif i < 0:
            lyst2.append(i)
    print(lyst1)
    print(lyst2)
xy(numbers)



rectors = [['Weder', 'Fischer', 'Jarren', 'Hengartner'],
 ['Hans', 'Andreas', 'Ottfried', 'Michael'],
 [2000, 2008, 2013, 2014]]
new_rector = ['Schaepmann', 'Michael', 2020]
def add(rector):    
    rectors[0].append(rector[0])
    rectors[1].append(rector[1])
    rectors[2].append(rector[2])
    print(rectors)

add(new_rector)


def affordable(lyst, number):
    count = 0
    for i in lyst:
        count += i
    if count <= number:
        return True
    return False

groceries = [2.50, 5.95, 0.6, 19.95, 3.20, 1.50]
limit = 30
if affordable(groceries, limit):
 print('You can afford it!')
else:
 print('Sorry, too expensive...')
 
 
 
with open('C:/Users/copet/Downloads/HS19_repeat_exam_answers/microbe_identifiers.txt') as f:
    f = f.readline().split()
    dic= {}
    for i in f:
        if i[i.find('-')+1:i.find('-')+3] not in dic:
            dic[i[i.find('-')+1:i.find('-')+3]] = []
        dic[i[i.find('-')+1:i.find('-')+3]].append(i[i.find('-')+1:])
    print(dic)


import numpy as np
im = np.array(
[[[0.7, 0.4, 0.2],[0.5, 0.8, 0.8],[0.1, 0.9, 0.2],[0.3, 0.4, 0.5]],
[[0.7, 0.3, 0.2],[0.4, 0.4, 0.8],[0.1, 0.8, 0.3],[0.9, 0.9, 0.3]]])


def minny(array):
    lyst = []
    lyst2  =[]
    for k,i in enumerate(array):
        for j in i:
            minn = float('inf')
            for n in j:
                if n < minn:
                    minn = n
            
            lyst.append(minn)
            
        lyst2.append(lyst)
        lyst= []
    print(np.array(lyst2))
minny(im)





hand_wash = 'You wash your hands properly by first wetting your hands under running water, soaping and rubbing your hands together until you get a lather. Rinse your hands thoroughly with running water. Dry the hands, with a clean towel, if possible a disposable paper towel or a cloth roller towel.' 
string = ''
for i in hand_wash:
    if i.isalpha() or i == ' ':
        string +=i
words = string.lower().split()
dic1 = {}
dic2 = {}
string
for j,i in enumerate(words):
    if i not in dic1:
        dic1[i] = 0
    dic1[i] += 1
    if i not in dic2:
        dic2[i] = []
    dic2[i].append(j)
        
mostcom = max(dic1.values())
for i in dic1:
    if dic1[i] == mostcom:
        mostcomword = i
for i in dic2:
    if i == mostcomword:
        mostcompos = dic2[i]
        
for i,j in enumerate(words):
    if i in mostcompos:
        words[i]=j.upper()
        words[i-1]= words[i-1].upper()
new_text= ' '.join(words)
print(f'Number of differnt words: {len(dic1)}')    
print(f'Most common word: {mostcomword}')
print(f'Its positions in the text: {mostcompos}')
print(new_text)


















































        
        
        
        
        
        
        
        
        
        
        
        