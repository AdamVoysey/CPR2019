#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys

def plot6Data(x, y1, y2, z1, z2, v1, v2):

    fig, ax = plt.subplots()
    xlim=[15,500]
    ax.set_xlim(xlim[0],xlim[1])
    width1=0.05*x

    rects1 = ax.bar(0.85*x, y1, width1, color='b',label="HET1",edgecolor='black')
    rects2 = ax.bar(0.9*x, y2, width1, color='r',label="HET6",edgecolor='black')
    
    rects3 = ax.bar(0.95*x, z1, width1, color='darkgreen',label="GST1",edgecolor='black')
    rects4 = ax.bar(x, z2, width1, color='teal',label="GST6",edgecolor='black')

    rects5 = ax.bar(1.05*x, v1, width1, color='purple',label="UT1",edgecolor='black')
    rects6 = ax.bar(1.1*x, v2, width1, color='pink',label="UT6",edgecolor='black')

    ax.set_xscale('log')
    ax.minorticks_on()
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")
    plt.show()
    
    
def plot2Data(x, y1, y2):

    fig, ax = plt.subplots()
    xlim=[15,500]
    ax.set_xlim(xlim[0],xlim[1])
    width1=0.1*x
    width2=0.1*x
    rects1 = ax.bar(0.95*x, y1, width1, color='firebrick',label="MPI",edgecolor='black')
    rects2 = ax.bar(1.05*x, y2, width2, color='goldenrod',label="OMP",edgecolor='black')
#    l1 = ax.plot(psx,psy,color='black',linestyle='dashed',label="perfect scaling")
    ax.legend(loc='upper right')
    ax.set_xscale('log')
#    ax.set_yscale('log')

 #   yax = [200, 400, 800, 1600, 3200]
 #   ax.set_yticks(yax)
    ax.minorticks_on()
    
    
    ax.set_xticks(x)
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")

#    fstem="strong-scale"
    fstem="wc-scale"
    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")    
    plt.show()


fname="perf.dat"
data=np.genfromtxt(fname, skip_header=1, usecols=range(0,7))
nodes=np.array(data[0:5,0])
print nodes
T6W=np.array(data[0:5,1])
T1W=np.array(data[5:10,1])

P6HE=np.array(data[0:5,2])
P1HE=np.array(data[5:10,2])

P6GS=np.array(data[0:5,3])
P1GS=np.array(data[5:10,3])

P6U=np.array(data[0:5,4])
P1U=np.array(data[5:10,4])

T6HE=T6W*P6HE
T1HE=T1W*P1HE

T6GS=T6W*P6GS
T1GS=T1W*P1GS

T6U=T6W*P6U
T1U=T1W*P1U


#nodes=np.array(sdata[:,0])
#mpidat=np.array(sdata[:,1])
#ompdat=np.array(sdata[:,2])

#plot2Data(nodes, T1W, T6W)

plot6Data(nodes, T1HE, T6HE, T1GS, T6GS, T1U, T6U)
