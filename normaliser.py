import numpy as np
import os
from PIL import Image, ImageFilter
import sys
import cv2
import glob

def load_paths(directory):
    paths = []
    for files in os.listdir(directory):
        if (files != ".DS_Store"):
            paths.append(directory+'/'+files)
    return paths

def blur(image):
    
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.fastNlMeansDenoisingColored(image,None,10,48,7,5)
    dst = cv2.filter2D(dst,-1,kernel)
    #blur = cv2.bilateralFilter(image,9,75,75)
    #blur = cv2.blur(image,(5,5))
    #blur = cv2.GaussianBlur(image,(5,5),0)
    return dst

def resize_and_save(path,size,directory):
    
    try:
        img = Image.open(path)
        img = img.resize(size)
        img.save(path, "JPEG")
        im = cv2.imread(path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        blurred = blur(im)
        img = Image.fromarray(blurred)
        #img = img.filter(ImageFilter.SHARPEN)
        img.save(directory, "JPEG")
    except IOError:
        print "cannot create thumbnail for '%s'" % path


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
classi = 0
for path in paths:
    print ("Processing class: "+str(float(classi)/len(paths)))
    classi = classi + 1
    temp = load_paths(path)
    for p in temp:
        elements = p.split('/')
        d = 'SGTSD/Images_blurred/'+elements[-2]+"/"+elements[-1]
        resize_and_save(p,(48,48), d)

