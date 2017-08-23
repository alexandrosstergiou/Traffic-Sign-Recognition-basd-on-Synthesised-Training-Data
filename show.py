import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
from os import listdir, getcwd
from os import chdir
from PIL import Image
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.image as mimage
from matplotlib.backends.backend_pdf import PdfPages



files = listdir('CNN_run2/Visualisations_w_folders/max_pooling_3')
chdir('CNN_run2/Visualisations_w_folders/max_pooling_3')


images = [Image.open(f).convert('LA') for f in files]


"""
    fig = plt.figure()
    
    grid = ImageGrid(fig, 111, # similar to subplot(111)
    nrows_ncols = (2, 5), # creates 2x2 grid of axes
    axes_pad=0.1, # pad between axes in inch.
    )
    """

num_rows = 1
num_cols = 128

fig = plt.figure()
gs = gridspec.GridSpec(num_rows, num_cols, wspace=0.0)

i = 0
for g in gs:
    ax = plt.subplot(g)
    ax.imshow(images[i])
    ax.set_xticks([])
    ax.set_yticks([])
    i = i + 1
#    ax.set_aspect('auto')

plt.axis('off')
plt.show()
