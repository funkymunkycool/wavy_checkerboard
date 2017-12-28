#!/usr/bin/env python

import numpy as np
from PIL import Image, ImageDraw


class checkerboard():

    def __init__(self):
        self.resolution = 1200                                  # Resolution of main image
        self.nGrid = 6                                          # Number of grids on checkerboard
        self.grid_size = self.resolution / self.nGrid           # Checkerboard spacing size
        self.grid_scale = 1.0

        self.scales = np.linspace(0.8,1.0,4)                    # Different sizes of checkerboard to be made

        self.dt = 2/60.                                         # Change in time. Shifts board by 2 squares
        self.dA = 2 * np.pi / 60.0                              # Change in angle. Shifts y axis by sin(2 pi)
        return None

    def make_figure(self):
        self.image = Image.new('RGB',(self.resolution,)*2,color='white')  #Setup PIL canvas with defined resolution
        return None

    def animate(self):
        for t in xrange(60):                                    # Loop over 60 times
            self.make_figure()                                  # Create a canvas
            drawer = ImageDraw.Draw(self.image)                 # Set up a PIL drawer
            for scale in self.scales:                           # Loop over different checkerboard sizes
                rectColor = (int((0.8-scale)*255),int(scale*255),int((1-scale)*255))    # Define color of rectangle based on its size
                for x in xrange(self.nGrid):                
                    for y in xrange(self.nGrid):                # Loop over the xy axes and plot rectangle in checkerboard pattern with size and color depending on its scale. Its position depends on time
                        if (x + y) % 2 == 0: 
                             drawer.rectangle(((x-(self.dt*t))*self.grid_size*scale,(y+np.sin(self.dA*t))*self.grid_size*scale,(x+1-(self.dt*t))*self.grid_size*scale,(y+1+np.sin(self.dA*t))*self.grid_size*scale),fill = rectColor)
            cropped = self.image.crop(( 35, 235,435,635))                    # Extract a smaller section of the figure
            cropped.save('checkerboard_images_PIL/checker_%03d.png' % t)     # Save to separate folder
        return None


if __name__ == '__main__':
    board = checkerboard()
    board.animate()
