#!/usr/bin/env python

import numpy as np
from PIL import Image, ImageDraw


class checkerboard():

    def __init__(self):
        self.resolution = 1200 
        self.nGrid = 6 
        self.grid_size = self.resolution / self.nGrid 
        self.grid_scale = 1.0

        self.scales = np.linspace(0.8,1.0,4)

        self.dt = 2/60. 
        self.dA = 0.105
        return None

    def make_figure(self):
        self.image = Image.new('RGB',(self.resolution,)*2,color='white')
        return None

    def animate(self):
        for t in xrange(60):
            self.make_figure()
            drawer = ImageDraw.Draw(self.image)
            for scale in self.scales:
                rectColor = (int((0.8-scale)*255),int(scale*255),int((1-scale)*255))
                for x in xrange(self.nGrid):
                    for y in xrange(self.nGrid):
                        if (x + y) % 2 == 0:
                             drawer.rectangle(((x-(self.dt*t))*self.grid_size*scale,(y+np.sin(self.dA*t))*self.grid_size*scale,(x+1-(self.dt*t))*self.grid_size*scale,(y+1+np.sin(self.dA*t))*self.grid_size*scale),fill = rectColor)
            cropped = self.image.crop(( 35, 235,435,635))
            cropped.save('checkerboard_images_PIL/checker_%03d.png' % t)
        return None


if __name__ == '__main__':
    board = checkerboard()
    board.animate()
