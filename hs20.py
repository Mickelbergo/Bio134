
#1
text = 'tgovoyd vlwucqk'
numbers = [3, 9, 7, 0, 9, 5, 7, 8, 2, 8, 3, 6, 7, 0, 6]

stringy = ''
for j,i in enumerate(numbers):
    if i > 5:
        stringy += text[j]
print(stringy)

#%%
#2

rna = 'AUGUUCGAA'

dic = {}
for j,i in enumerate(rna):
    if i not in dic:
        dic[i] = []
    dic[i].append(j)

print(dic)

#%%
#3

import numpy as np
np.random.seed(0)
def n_times_to_threshold(thresh, maximum):
    summy = 0
    counter = 0
    for i in range(thresh):
        if summy < thresh:
            summy += np.random.randint(1, maximum+1)
            counter += 1
        else:
            return counter
k = n_times_to_threshold(43, 10)
print('The '+str(k)+'th number has brought the sum above the threshold!')

#%%
#4
import numpy as np
data = np.zeros([5,12])
rowcount = 0
columncount = 0
with open('fMRI_series.txt') as f:
    
    for j,i in enumerate(f.readlines()):
        line = i.split()
        if int(line[0]) < 170:
            continue
        if (int(line[0])-110)% 60 == 0:
            rowcount+=1
            columncount= 0 
        if rowcount >0:
            data[rowcount-1][columncount] += float(line[1])
            columncount +=1
            
print(np.mean(data,0))
#%%


    
#5

planets = [['Earth', 12742, 149598262], ['Jupiter', 139822,778340821], ['Mars', 6779, 227943824], ['Mercury', 4878, 57909227],['Neptune', 49244, 4498396441], ['Saturn', 116464, 1426666422],['Uranus', 50724, 2870658186], ['Venus', 12104, 108209475]]

planets.sort(key = lambda distance: distance[2])
long2 = len(str(planets[-1][-1]))
diameter = [plan for planet in planets for i,plan in enumerate(planet) if i == 1]
long = len(str(max(diameter)))
for j,i in enumerate(planets):
    if j == 0:
        print(i[0] + '.' * (10-len(i[0])) + ' ' * (long-len(str(i[1]))+1) + str(i[1]) + ' km in diameter ' + ' ' * (long2-len(str(i[2]))) + str(i[2]) + ' km away from the sun')
    else:
        print(i[0] + '.' * (10-len(i[0])) +' ' * (long-len(str(i[1]))+1) +  str(i[1]) + ' ' + '*' * 14 + ' ' + ' ' * (long2-len(str(i[2])))+ str(i[2]) + ' ' + '*' * 21)      
        
#%%      
#6
import numpy as np

functional_motifs = ['GAGGTAAAC','TCCGTAAGT','AAGGTTGGA','ACAGTCAGT','TAGGTCATT', 'TAGGTACTG','ATGGTAACT','CAGGTATAC','TGTGTGAGT','AAGGTAAGT']

query ='ACTCAGCCCCAGCGGAGGTGAAGGACGTCCTTCCCCAGGAGCCGGTGAGAAGCGCAGTCGGGGGCACGGGGATGAGCTCAGGGGCCTCTAGAAAGATGTAGCTGGGACCTCGGGAAGCCCTGGCCTCCAGGTAGTCTCAGGAGAGCTACTCAGGGTCGGGCTTGGGGAGAGGAGGAGCGGGGGTGAGGCCAGCAGCA'

#generate matrix
matrix  = np.zeros([4,len(functional_motifs[0])])

dic = {'A': 0, 'C': 0, 'G':0, 'T': 0}
for index in range(len(functional_motifs[0])):
    for i,j in enumerate(functional_motifs):
        dic[j[index]] += 1
    matrix[0][index] += (dic['A']/len(functional_motifs))
    matrix[1][index] += (dic['C']/len(functional_motifs))
    matrix[2][index] += (dic['G']/len(functional_motifs))
    matrix[3][index] += (dic['T']/len(functional_motifs))
    dic = {'A': 0, 'C': 0, 'G':0, 'T': 0}
   
        
print(matrix)

#find score larger than 4.4
score = 0
for i in range(len(query)):
    for index,value in enumerate(query[i:i+9]):
        if value == 'A':
            score += matrix[0][index] 
        elif value == 'C':
            score += matrix[1][index]
        elif value == 'G':
            score +=matrix[2][index]
        else:
            score += matrix[3][index]
            
    if score > 4.4:
        print(f'position {i}: {query[i:i+9]}, {score}')
        
    score =0
    
    
#find ideal motif
idealmotif = ''
dic = {0:'A', 1:'C', 2:'G', 3:'T'}
x = np.amax(matrix, axis = 0) #finds the max value for each column


for index in range(len(matrix[0])):
    for columnindex, columnvalue in enumerate(matrix):
        if columnvalue[index] == x[index]:
            idealmotif += dic[columnindex]
            break
            
print(idealmotif)


#%%
#7
from string import ascii_lowercase

aminoacids=['alanine','cysteine','aspartic acid','glutamic acid',
'phenylalanine','glycine','histidine','isoleucine','lysine',
'leucine','methionine','asparagine','proline','glutamine',
'arginine','serine','threonine','valine','tryptophan','tyrosine']

aminoacids.sort(key = lambda length: len(length)) #sort by length
dic = {}
for i in range(len(aminoacids)):
    for j in aminoacids:
        if j[0] not in dic:
            dic[j[0]] = j[0].upper() + j[1:]
            
        
dic2 = {i:j for i,j in enumerate(ascii_lowercase)}
aminoacids.sort() #sort alphabetically

for index,remaining in enumerate(aminoacids):
    if remaining in dic[remaining[0]].lower():
        continue
    
    indi = 0
    for i in range(26):
        if dic2[indi] in dic:
            indi +=1
        else:
            dic[dic2[indi]] = remaining[0].upper() + remaining[1:]
            break
        

for i in ascii_lowercase:
    if i not in dic:
        print(i, '_ _ _')
    else:
        print(i,dic[i])
        
        
        