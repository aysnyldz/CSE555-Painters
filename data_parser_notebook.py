#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[4]:


path ="all/all_data_info.csv"


# In[5]:


with open(path) as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        data = [r for r in reader]


# In[14]:


listArtistFile=[] #artist,new_filename
artists =[] #artist list


# In[15]:


for i in data:
    listTrain=(i['artist'], i['new_filename'])
    listArtistFile.append(listTrain)
    artists.append(i['artist'])

artists = list(set(artists)) #artist unique list
#print(len(artists))


# In[16]:


galeries=[]
for k in range(len(artists)):
    picturesName = []
    c=0
    for j in listArtistFile:
        if(j.__getitem__(0)== artists[k]):
            picturesName.append(j.__getitem__(1))
            c+=1
    if c==500 :
        galerie=(artists[k],picturesName)
        galeries.append(galerie)


# In[17]:


print(len(galeries))

print(galeries[0].__getitem__(0), galeries[0].__getitem__(1) )


# In[18]:


import glob


# In[49]:


import os
import shutil



train_root="all/train"
test_root="all/test"

#print(train_root+train_index)


data_list = galeries[0].__getitem__(1)
#for data in data_list:
        #print(data)

for x in range(0,len(galeries)):
    directory = "labels/"+galeries[x].__getitem__(0)
    if not os.path.exists(directory):
        os.makedirs(directory)
    data_list = galeries[x].__getitem__(1)
    count = 0
    for data in data_list:
        #print(train_root)
        #print(data)
        #print(train_root+"/"+data)
        path = glob.glob(train_root+"/"+data)
        if not path:
            path = glob.glob(test_root+"/"+data)
        
        #print(path[0])
        #print(directory)
        directory = "labels/"+galeries[x].__getitem__(0)
        if count < 300:
            directory+="_train"
            if not os.path.exists(directory):
                os.makedirs(directory)
        elif count>=300 and count<400:
            directory+="_validation"
            if not os.path.exists(directory):
                os.makedirs(directory)
        else:
            directory+="_test"
            if not os.path.exists(directory):
                os.makedirs(directory)
            
        shutil.copy2(path[0],directory)
        count+=1


#print(list)


# In[126]:


import cv2
import random
img = cv2.imread("labels/Pablo Picasso_train/91407.jpg")

width = len(img[0])
height = len(img)

croppy = 300

def generateRandomPoints(width,height):
    rand_x = random.randint(0,width)
    rand_y = random.randint(0,height)
    print(width)
    print(height)
    print(rand_x)
    print(rand_y)
    if (rand_x + croppy < width) and (rand_y + croppy < height):
        return rand_x,rand_y
    return generateRandomPoints(width,height)
     
        
core_x,core_y = generateRandomPoints(width,height)

print(core_x,core_y)
crop_img = img[core_y:core_y+croppy, core_x:core_x+croppy]
cv2.imshow("cropped", crop_img)
print(crop_img.shape)
cv2.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:




