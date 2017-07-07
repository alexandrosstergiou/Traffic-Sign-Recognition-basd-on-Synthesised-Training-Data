import numpy as np
import os
from PIL import Image
import sys

def load_paths(directory):
    paths = []
    for files in os.listdir(directory):
        if (files != ".DS_Store"):
            paths.append(directory+'/'+files)
    return paths



def resize_and_save(path,size):

    head,tail = path.split('.')
    output = head+".jpg"
    try:
        img = Image.open(path)
        img = img.resize(size)
        os.remove(path)
        img.save(output, "JPEG")
    except IOError:
        print "cannot create thumbnail for '%s'" % infile

paths = load_paths("val_set")
for path in paths:
    temp = load_paths(path)
    for p in temp:
        resize_and_save(p,(48,48))
