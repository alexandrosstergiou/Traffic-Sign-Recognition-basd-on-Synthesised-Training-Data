import numpy as np
import os
from PIL import Image
import sys
import cv2

def load_paths(directory):
    paths = []
    for files in os.listdir(directory):
        if (files != ".DS_Store"):
            paths.append(directory+'/'+files)
    return paths

def blur(image):
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(image,-1,kernel)
    #blur = cv2.bilateralFilter(image,9,75,75)
    return dst

def resize_and_save(path,size,directory):
    
    try:
        img = Image.open(path)
        img = img.resize(size)
        im = np.uint8(img)
        blurred = blur(im)
        img = Image.fromarray(blurred)
        img.save(directory, "JPEG")
    except IOError:
        print "cannot create thumbnail for '%s'" % infile


directory = 'val_set_blurred'
if (not os.path.exists('val_set_blurred')):
    for sign in load_paths("Traffic_Signs_Templates/Images"):
        head,tail = sign.split('.')
        name = []
        name = head.split('/')
        os.makedirs('val_set_blurred/'+name[-1])




paths = load_paths("val_set")
for path in paths:
    temp = load_paths(path)
    for p in temp:
        elements = p.split('/')
        d = 'val_set_blurred/'+elements[-2]+"/"+elements[-1]
        resize_and_save(p,(48,48), d)



directory = 'SGTSD/Images_blurred/'
if (not os.path.exists('SGTSD/Images_blurred/')):
    for sign in load_paths("Traffic_Signs_Templates/Images"):
        head,tail = sign.split('.')
        name = []
        name = head.split('/')
        os.makedirs('SGTSD/Images_blurred/'+name[-1])


paths = load_paths("SGTSD/Images/")
for path in paths:
    temp = load_paths(path)
    for p in temp:
        elements = p.split('/')
        d = 'SGTSD/Images_blurred/'+elements[-2]+"/"+elements[-1]
        resize_and_save(p,(48,48), d)

