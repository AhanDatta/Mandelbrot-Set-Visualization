#This program visualizes the Mandelbrot set
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors
import math
import cmath

#Value which defines the line between divergence and convergence
DIV_VALUE = 2
DIV_VALUE_SQUARE = DIV_VALUE ** 2
#Sets the resolution of sampling 
RESOLUTION = 0.005
#Sets the iteration count when checking divergence
ITERATION_COUNT = 1000
#Setting the window dimensions
MIN_WINDOW = complex(-2.,-2.)
MAX_WINDOW = complex(2.,2.)

#The function which defines the Mandelbrot set with a complex variable z and a changable complex constant c
def f (z, c):
    try:
        return z**2 + c
    except OverflowError:
        return float('inf')

#Applies f iteratively with a complex constant c, and returns the iteration on which the value diverged or ITERATION_COUNT
def iterated_f (c):
    value = c
    iter = 0
    while iter < ITERATION_COUNT:
        if value == float('inf') or (value.real**2 + value.imag**2) > DIV_VALUE_SQUARE:
            break
        value = f(value, c)
        iter += 1
    return iter

def does_diverge(c):
    num_iter = iterated_f(c)
    if num_iter == ITERATION_COUNT:
        return True
    else:
        return False

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


#Creating a black and white visualization of the set.
cmap = matplotlib.colors.ListedColormap(['white', 'black'])
plt.imshow(div_grid, cmap=cmap, interpolation='hermite')
plt.axis('off')
plt.title("Mandelbrot Set")
plt.show()