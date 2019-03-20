#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

import sys

data=np.array([9.45,5.33,2.68,0.58,0.32])
temp_data=np.array(data[1:5])
sp_data=data[0]/temp_data
xdata=np.array([1,2,3,4])

print sp_data

fig, ax = plt.subplots()
ax.set_xlim(0.2,4.8)
rects = ax.bar(xdata, sp_data, 0.5, color='teal',edgecolor='black')
ax.set_xlabel("Optimisations")
ax.set_ylabel("Speed up")

plt.savefig("LMA-nvidia.png",format="png")
plt.savefig("LMA-nvidia.eps",format="eps")
plt.show()
