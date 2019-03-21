#!/usr/local/bin/python
"""Generate plots for "vanilla" benchmark on Broadwell and TX2
"""
import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt

# these are small plots so use larger fonts
plt.rcParams.update({'font.size': 16})

# load in the data.
xc_cce, xc_intel, xc_gnu, tx2_cce, tx2_gnu, tx2_arm = \
    np.genfromtxt('cma_vanilla.dat')

ydata = ([xc_cce, xc_intel, xc_gnu],
         [tx2_cce, tx2_gnu, tx2_arm])

ylabels = (['CCE 8.7.7', 'Intel 17.0.0', 'GNU 7.3.0'],
           ['CCE 8.7.9', 'Allinea 19.0.1', 'GNU 8.2.0'])

ycolours = (['teal', 'navy', 'lightskyblue'],
            ['teal', 'mediumpurple', 'lightskyblue'])

names = ('Broadwell', 'ThunderX2')

xdata = np.arange(len(xc_cce))
bar_width = 0.25

for data, labels, colours, name in zip(ydata, ylabels, ycolours, names):

    fig, ax = plt.subplots()

    ax.bar(xdata, data[0], bar_width,
           color=colours[0], edgecolor='black',
           label=labels[0])

    ax.bar(xdata + bar_width, data[1], bar_width,
           color=colours[1], edgecolor='black',
           label=labels[1])

    ax.bar(xdata + 2 * bar_width, data[2], bar_width,
           color=colours[2], edgecolor='black',
           label=labels[2])

    ax.set_xlabel("Threads")
    ax.set_ylabel("Time (ms)")
    ax.legend()
    # centre the tick marks
    ax.set_xticks(xdata + bar_width)
    ax.set_xticklabels(('1', '2', '4', '8', '16', '32', 'Node'))
    fig.tight_layout()

    pltname = name + "_microbenchmark_vanilla"
    fig.savefig(pltname + ".png", format="png")
    fig.savefig(pltname + ".eps", format="eps")

plt.show()
