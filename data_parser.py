#!/usr/bin/env python
# coding: utf-8
import csv
import cv2
import random
import glob

import os


path = "../all/all_data_info.csv"
train_root = "../all/train"
test_root = "../all/test"


def load_galeries() :
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            data = [r for r in reader]

    listArtistFile = []  # artist,new_filename
    artists = []  # artist list

    for i in data:
        listTrain = (i['artist'], i['new_filename'])
        listArtistFile.append(listTrain)
        artists.append(i['artist'])

    artists = list(set(artists))  # artist unique list
    # print(len(artists))

    galeries = []
    for k in range(len(artists)):
        picturesName = []
        c = 0
        for j in listArtistFile:
            if (j.__getitem__(0) == artists[k]):
                picturesName.append(j.__getitem__(1))
                c += 1
        if c == 500:
            galerie = (artists[k], picturesName)
            galeries.append(galerie)

    #print(len(galeries))
    #print(galeries[0].__getitem__(0), galeries[0].__getitem__(1))
    return galeries




import shutil



# print(train_root+train_index)

"""galeries = load_galeries()
data_list = galeries[0].__getitem__(1)"""
# for data in data_list:
# print(data)

def generateRandomPoints(width, height,croppy):
    rand_x = random.randint(0, width)
    rand_y = random.randint(0, height)
    #print(width)
    #print(height)
    #print(rand_x)
    #print(rand_y)
    if (rand_x + croppy < width) and (rand_y + croppy < height):
        return rand_x, rand_y
    return generateRandomPoints(width, height,croppy)


def generatePatches(image,cropSize,patchNumber,filename,patchdir) :
    if not os.path.exists(patchdir):
        os.makedirs(patchdir)
    width = len(image[0])
    height = len(image)
    for patches in range(0,patchNumber) :
        rand_x, rand_y = generateRandomPoints(width, height, cropSize)
        #print(rand_x, rand_y)
        crop_img = img[rand_y:rand_y + cropSize, rand_x:rand_x + cropSize]
        fname = patchdir + "/" + str(patches) + "-" + filename
        cv2.imwrite(fname, crop_img)

"""for x in range(0, len(galeries)):
    directory = "../data/" + galeries[x].__getitem__(0)
    if not os.path.exists(directory):
        os.makedirs(directory)
    data_list = galeries[x].__getitem__(1)
    count = 0
    for data in data_list:
        # print(train_root)
        # print(data)
        # print(train_root+"/"+data)
        #print(data)
        path = glob.glob(train_root + "/" + data)
        if not path:
            path = glob.glob(test_root + "/" + data)

        # print(path[0])
        # print(directory)
        img = cv2.imread(path[0])
        directory = "../data/" + galeries[x].__getitem__(0)

        if count < 300:
            directory += "_train"
            patchdir = directory + "/patches"
            if not os.path.exists(directory):
                os.makedirs(directory)

            generatePatches(img, 300, 100, data, patchdir)
        elif count >= 300 and count < 400:
            directory += "_validation"
            patchdir = directory + "/patches"
            if not os.path.exists(directory):
                os.makedirs(directory)
            generatePatches(img, 300, 100, data, patchdir)
        else:
            directory += "_test"
            patchdir = directory + "/patches"
            if not os.path.exists(directory):
                os.makedirs(directory)
            generatePatches(img, 300, 100, data, patchdir)

        #shutil.copy2(path[0], directory)
        count += 1"""

# print(list)


#img = cv2.imread("labels/Pablo Picasso_train/91407.jpg")

#width = len(img[0])
#height = len(img)

#croppy = 300





#core_x, core_y = generateRandomPoints(width, height)

#print(core_x, core_y)
#crop_img = img[core_y:core_y + croppy, core_x:core_x + croppy]
#cv2.imshow("cropped", crop_img)
#print(crop_img.shape)
#cv2.waitKey(0)



        #cv2.imshow("cropped", crop_img)

    #print(crop_img.shape)
    #cv2.waitKey(0)

