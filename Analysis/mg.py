#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

def plotData(x, y1, y2, y3, y4):

    fig, ax = plt.subplots()
    width1=0.1
    ylim=[0,2000]
#    ax.set_ylim(ylim[0],ylim[1])
    rects1 = ax.bar((x-0.1), y1, width1, color='tan',label="WC",edgecolor='black')
    rects2 = ax.bar(x, y2, width1, color='salmon',label="U",edgecolor='black')
    rects3 = ax.bar((x+0.1), y3, width1, color='firebrick',label="HE",edgecolor='black')
    rects4 = ax.bar((x+0.2), y4, width1, color='goldenrod',label="GS",edgecolor='black')
    ax.legend(loc='upper right')
    plt.xticks([1,2,3],["T","Kr","MG"])
    ax.set_ylabel("time (s)")    


    fstem="mg-improvement"
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")    
    plt.show()


fname="MG.dat"
data=np.genfromtxt(fname, skip_header=1, usecols=range(0,5))

cat=np.array(data[:,0])
wc=np.array(data[:,1])
u=np.array(data[:,2])
he=np.array(data[:,3])
gs=np.array(data[:,4])

plotData(cat, wc, u, he, gs)

