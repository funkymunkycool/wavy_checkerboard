#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

grid_size = np.arange(16)
grid_scale = 1.0

scales = np.linspace(0.6,1.0,4)

dt = 0.033
dA = 0.105


for t in xrange(60):
    fig,axes = plt.subplots()
    for scale in scales:
        for x in grid_size:
            for y in grid_size:
                if (x + y) % 2 == 0:
                    axes.add_patch(patches.Rectangle(((x-dt*t)*scale,(y+np.sin(dA*t))*scale),scale,scale,edgecolor = 'none',facecolor = (scale,scale,1-scale),alpha = scale))
    axes.set_xlim((6,8))
    axes.set_ylim((6,8))
    plt.axis('off')
    fig.savefig('checker_%03d.png' % t)
    plt.close()
