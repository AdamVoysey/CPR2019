#!/usr/local/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import math

import sys

def plot4Data3d(x, y1, y2, y3, y4,fstem):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xlim=[4,9]
    ax.set_xlim(xlim[0],xlim[1])
    width1=0.25 
    yticks=[1,2,3,4]

    rects1 = ax.bar(x, y1, zs=1, width=width1, zdir='y',color='hotpink',alpha=0.8,edgecolor='black')
    rects2 = ax.bar(x, y2, zs=2, width=width1, zdir='y', color='purple',alpha=0.8,edgecolor='black')
    rects3 = ax.bar(x, y3, zs=3, width=width1, zdir='y', color='teal',alpha=0.8,edgecolor='black')
    rects4 = ax.bar(x, y4, zs=4, width=width1, zdir='y', color='navy',alpha=0.8,edgecolor='black')

    ax.minorticks_on()
    ax.set_xticks(x)

    ax.legend(loc='upper right')    
    ax.set_xlabel("# nodes")
    ax.set_zlabel("time (s)")
    ax.set_yticks(yticks)
    plt.xticks([4.58496250072,5.75488750216,6.58496250072,7.75488750216,8.58496250072],["24","54","96","216","384"])
    plt.yticks([1,2,3,4],["HET1", "HET6","GST1", "GST6"])

    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")      
    plt.show()
###########################################    

def plot4Data(x, y1, y2, y3, y4,fstem):

    fig, ax = plt.subplots()    
    xlim=[15,500]
    ax.set_xlim(xlim[0],xlim[1])
    width1=0.1*x

    rects1 = ax.bar(0.8*x, y1, width1, color='hotpink',label="HE MPI",edgecolor='black')
    rects2 = ax.bar(0.9*x, y2, width1, color='purple',label="HE OMP",edgecolor='black')
    rects3 = ax.bar(x, y3, width1, color='teal',label="GS MPI",edgecolor='black')
    rects4 = ax.bar(1.1*x, y4, width1, color='navy',label="GS OMP",edgecolor='black')

    ax.set_xscale('log')
    ax.minorticks_on()
    ax.set_xticks(x)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.get_xaxis().set_minor_locator(ticker.NullLocator())

    ax.legend(loc='upper right')    
    ax.set_xlabel("# nodes")
    ax.set_ylabel("time (s)")

    fname=fstem+".png"
    plt.savefig(fname,format="png")
    fname=fstem+".eps"
    plt.savefig(fname,format="eps")      
    plt.show()    
    
    
def plot2Data(x, y1, y2,fstem):

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

lnodes=[0,0,0,0,0]
for i in range(0,5):
    lnodes[i]=math.log(nodes[i],2)

for i in range(1,5):
    print str(nodes[i]/nodes[0]) + " " + str(T6W[0]/T6W[i] ) + " " + str(T1W[0]/T1W[i])

print "----"
for i in range(0,5):
    print "$"+str(nodes[i])+ "$ & $" + str(T1W[i]) + "$ & $" + str(T1U[i]) + "$ & $" + str(T1HE[i]) + "$ & $" + str(T1GS[i]) + "$ & $$ & $$ & $"+ str(T6W[i]) + "$ & $" + str(T6U[i]) + "$ & $" + str(T6HE[i]) + "$ & $" + str(T6GS[i]) + "$ & $$ & $$ \\\\"

#plot2Data(nodes, T1W, T6W,"wc-scale")
#plot2Data(nodes, T1U, T6U,"U-scale")
#plot4Data3d(lnodes, T1HE, T6HE, T1GS, T6GS,"comms-scale-3d")
#plot4Data(nodes, T1HE, T6HE, T1GS, T6GS,"comms-scale")
