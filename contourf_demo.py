import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import os

print("Input file name")
filename = input().strip()

# check whether file exist before opening
if not filename in os.listdir() :
    raise Exception("Cannot find file %s: maybe you are missing an extension?" % filename)

# z is our data : an array of array
# we read the datafile to our variable z
z = np.loadtxt(filename)

# this is the number of countour lines
n_contour_lines = 7

# distance per seperation of loads
# if each load is 2 cm apart from each other, the value is 2
distance_per_sep = 1

# Resample / interpolate
resample_factor = 10
z = scipy.ndimage.zoom(z, 10)
# zoom will change the size of the array, so we have to set the size back
y_range = np.arange(0, z.shape[0]) / resample_factor
x_range = np.arange(0, z.shape[1]) / resample_factor

# plot

plt.title("Weight of each sensor input (in kg)")
# contour plotting fuction return the contour information
contour_set = plt.contourf(x_range, y_range, z, n_contour_lines)
# use that information to create a color bar on the side
plt.colorbar(contour_set)
# reverse the y-axis
plt.gca().invert_yaxis()

plt.xlabel("distance (cm)")
plt.ylabel("distance (cm)")
plt.show()

