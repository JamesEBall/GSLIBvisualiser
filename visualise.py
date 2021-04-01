import numpy as np
import matplotlib.pyplot as plt
import linecache
from mpl_toolkits.mplot3d import Axes3D


class GSlib:
    def __init__(self, input):
        self.gslib = open(input, "r")
    
    #initiate first to get xyz and facies data
    def xyparse():
        firstline = linecache.getline(self.gslib, 1) #read line 1
        xyz = [int(firstline) for firstline in str.split() if firstline.isdigit()]
        #file is x,y,z
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]
        self.faciesinputlines = input.readline()

        self.facies = []
        for i in lines:
            self.facies.append(line = str.split(input.readline()))

    def gslibtoarray(self):
        array = []
        xrow = self.faciesinputlines + 2 #start on data value line
        for zzrow in range(0,self.z):
            for yxrow in range(0,self.y):
                for xrow in range(0,self.x):
                    linecache.getline
        return array


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# your real data here - some 3d boolean array
x, y, z = np.indices((10, 10, 10))
voxels = (x == y) | (y == z)

ax.voxels(voxels)

plt.show()