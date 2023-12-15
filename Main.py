#This program visualizes the Mandelbrot set
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors
import math
import cmath

#Value which defines the line between divergence and convergence
DIV_VALUE = 2
#Sets the resolution of sampling 
RESOLUTION = 0.001
ITERATION_COUNT = 50
#Setting the window dimensions
MIN_WINDOW = complex(-2.,-2.)
MAX_WINDOW = complex(2.,2.)

#The function which defines the Mandelbrot set with a complex variable z and a changable complex constant c
def f (z, c):
    try:
        return z**2 + c
    except OverflowError:
        return float('inf')

#Applies f iteratively with a complex constant c
def iterated_f (c):
    value = c
    for i in range(ITERATION_COUNT):
        value = f(value, c)
    return value

def does_diverge(c):
    value = np.absolute(iterated_f(c))
    if value <= DIV_VALUE:
        return False
    else:
        return True

#Grid of possible values for c, containing whether they converge or diverge
div_grid =[]
current_imag = MIN_WINDOW.imag
for i1 in range(math.ceil((MAX_WINDOW.real - MIN_WINDOW.real)/RESOLUTION)):
    current_real = MIN_WINDOW.real
    div_grid.append([])
    for i2 in range(math.ceil((MAX_WINDOW.imag - MIN_WINDOW.imag)/RESOLUTION)):
        div_grid[i1].append(does_diverge(complex(current_real, current_imag)))
        current_real += RESOLUTION
    current_imag += RESOLUTION



#Creating a color-coded visualization of the set.
cmap = matplotlib.colors.ListedColormap(['black', 'white'])
plt.imshow(div_grid, cmap=cmap, interpolation='hermite')
plt.axis('off')
plt.title("Mandelbrot Set")
plt.show()