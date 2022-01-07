
#1

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

#%%
#2
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
#%%
#3
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
 
#%%
#4
 
with open('C:/Users/copet/Downloads/HS19_repeat_exam_answers (1)/HS19_repeat_exam_answers/microbe_identifiers.txt') as f:
    f = f.readline().split()
    dic= {}
    for i in f:
        if i[i.find('-')+1:i.find('-')+3] not in dic:
            dic[i[i.find('-')+1:i.find('-')+3]] = []
        dic[i[i.find('-')+1:i.find('-')+3]].append(i[i.find('-')+1:])
    print(dic)
    
#%%
#5

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

#%%

#6
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
print(f'Number of different words: {len(dic1)}')    
print(f'Most common word: {mostcomword}')
print(f'Its positions in the text: {mostcompos}')
print(new_text)



#7 to be done
#%%
with open('C:/Users/copet/Downloads/HS19_repeat_exam_answers (1)/HS19_repeat_exam_answers/microbial_samples.txt') as f:
    dic = {}
    summy2 = 0
    for i in f.readlines():
        if i[:i.find(' ')] not in dic:
            dic[i[:i.find(' ')]] = []
        dic[i[:i.find(' ')]].append(i[i.find(' '):])
    for i in dic:
        for j in dic[i]:
            seq = j.split()
            lyst = [[] for _ in range(len(seq)+1)]
            for k,j in enumerate(seq):
                seq[k] = int(j)
            summy = sum(seq)
            
            if summy > summy2: 
                summy2= summy
                place = i
                
    f.seek(0)
    for m in f.readlines():
        seq = m.split()
        for x,y in enumerate(seq):
            lyst[x].append(y)
        
print(f'The sample with the most microbes, {summy2} counts, comes from the {place}')



microbe_ids = ['S97-ac103', 'S97-ga105', 'S97-cy13', 'S97-ac137','S97-de22', 'S97-de227', 'S97-cy30', 'S97-fi362', 'S97-ga404','S97-fi47', 'S97-ac51', 'S97-ac769', 'S97-fi77', 'S97-ga86']




#%%
#7
#create matrices
import numpy as np
oralcount = 0
gutcount = 0
skincount = 0
with open('C:/Users/copet/Downloads/HS19_repeat_exam_answers (1)/HS19_repeat_exam_answers/microbial_samples.txt') as f:
    for line in f.readlines():
        line = line.split()
        microbecount = len(line[1:])
        if line[0] == 'Oral':
            oralcount += 1
        elif line[0] == 'Gut':
            gutcount += 1
        else:
            skincount += 1
    oral = np.zeros([oralcount, microbecount])
    gut = np.zeros([gutcount, microbecount])
    skin = np.zeros([skincount, microbecount])

#fill up the matrices with all abundencies
    f.seek(0) #get back to the start of the file
    oralcount = 0
    gutcount = 0
    skincount = 0
    skinn=False
    orall =False
    gutt =False
    for line in f.readlines():
        line = line.split()
        for index, value in enumerate(line):
            if value =='Skin':
                skinn = True
                continue
            
            elif value == 'Oral':
                orall = True
                continue

            elif value == 'Gut':
                gutt = True
                continue

            if skinn:
                skin[skincount][index-1] += int(value)

            if orall:
                oral[oralcount][index-1] += int(value)
                
            if gutt:    
                gut[gutcount][index-1] += int(value)
        if skinn:
            skincount+=1
        elif orall:
            oralcount+=1
        else:
            gutcount+=1
        skinn, orall, gutt = False,False,False
    
#get the maximum abundancy of each body site
maxxoral = np.sum(oral, axis = 1)
maxxoral = max(maxxoral)
maxxgut = np.sum(gut, axis = 1)
maxxgut = max(maxxgut)
maxxskin = np.sum(skin, axis = 1)
maxxskin = max(maxxskin)


if maxxskin > maxxgut and maxxskin > maxxoral:
    maxmicrobe = 'Skin'
    maxcount= maxxskin
elif maxxgut > maxxskin and maxxgut > maxxoral:
    maxmicrobe = 'Gut'
    maxcount = maxxgut
else:
    maxmicrobe = 'Oral'
    maxcount = maxxoral

#get the mean for every microbe 
oralsum =np.mean(oral, axis = 0)
gutsum = np.mean(gut, axis = 0)
skinsum =np.mean(skin, axis = 0)

microbe_ids = ['S97-ac103', 'S97-ga105', 'S97-cy13', 'S97-ac137',\
'S97-de22', 'S97-de227', 'S97-cy30', 'S97-fi362', 'S97-ga404',\
'S97-fi47', 'S97-ac51', 'S97-ac769', 'S97-fi77', 'S97-ga86']
  
    

orallist = [(microbe, summ) for index,microbe in enumerate(microbe_ids) for indexx, summ in enumerate(oralsum) if index == indexx]
gutlist = [(microbe, summ) for index,microbe in enumerate(microbe_ids) for indexx, summ in enumerate(gutsum) if index == indexx]
skinlist= [(microbe, summ) for index,microbe in enumerate(microbe_ids) for indexx, summ in enumerate(skinsum) if index == indexx]

#sort them by abundancy (most abundant at last place)
orallist.sort(key = lambda maxx: maxx[1])
gutlist.sort(key = lambda maxx: maxx[1])
skinlist.sort(key = lambda maxx: maxx[1])

mostoral = [orallist[-3][0],orallist[-2][0], orallist[-1][0]]
mostgut =  [gutlist[-3][0],gutlist[-2][0], gutlist[-1][0]]
mostskin =  [skinlist[-3][0],skinlist[-2][0], skinlist[-1][0]]
mostabundant = []
for i in mostoral:
    for j in mostgut:
        for k in mostskin:
            if i == j and i == k:
                mostabundant.append((i, 'Oral', 'Gut', 'Skin'))
            elif i == j:
                mostabundant.append((i, 'Oral', 'Gut'))
            elif i == k:
                mostabundant.append((i, 'Oral', 'Skin'))
            
            elif j == k:
                mostabundant.append((j, 'Gut', 'Skin'))
                
finalabundency = list(set(mostabundant))

     
print(f'The sample with the most microbes, {maxcount} counts, comes from the {maxmicrobe}')                     
print('The top 3 on average most abundant microbes per body site:')
print(f'Oral: {orallist[-1]} {orallist[-2]} {orallist[-3]}')
print(f'Gut: {gutlist[-1]} {gutlist[-2]} {gutlist[-3]}')
print(f'Skin: {skinlist[-1]} {skinlist[-2]} {skinlist[-3]}')    
if len(finalabundency)>1:
    print(f'{[i[0] for i in finalabundency]} are among the most abundant microbes in {[i[1:] for i in finalabundency]} ')
else:
    print(f'{finalabundency[0][0]} is among the most abundant microbes in {[i[1:] for i in finalabundency]}')





        
        
        
        
        
        
        
        
        
        
        
        