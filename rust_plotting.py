#This program takes the excel file from the rust program and plots it
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
from math import ceil

#Copy over from the rust file if need, but there is no need to change 
Z_MIN = -2.0 - 1.5j
Z_MAX = -Z_MIN
WINDOW_HEIGHT = 1080
WINDOW_WIDTH = 1440

#Set this based on your specific monitor, found at this link https://www.infobyip.com/detectmonitordpi.php
my_dpi = 144

#Gets file data and turns it into an array
try:
    set_data = pd.read_excel('mandelbrot_output.xlsx')
except PermissionError:
    print("Please close the excel file and try again.")
    sys.exit([-1])
plotting_array = np.array(set_data)

#Sets the color and does the plotting
color = mpl.colormaps['seismic']
plt.figure(figsize=(ceil(WINDOW_WIDTH/my_dpi), ceil(WINDOW_HEIGHT/my_dpi)), dpi=my_dpi)
plt.imshow(plotting_array, cmap=color, interpolation='none')
plt.axis('off')
plt.show()