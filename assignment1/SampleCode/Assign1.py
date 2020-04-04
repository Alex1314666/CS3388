from math import *
import numpy as np
from matrix import matrix
from graphicsWindow import graphicsWindow

t = 0.0
dt = 2.0*pi/200.0
color = (255,255,255)
p1 = matrix(np.zeros((2,1)))
p2 = matrix(np.zeros((2,1)))
window = graphicsWindow(512,512)
while t < 2.0*pi:
    p1.set(0,0,256 + int(100.0*(1.5*cos(t) - cos(13.0*t))))
    p1.set(1,0,256 + int(100.0*(1.5*sin(t) - sin(13.0*t))))

    t += dt
    p2.set(0,0,256 + int(100.0*(1.5*cos(t) - cos(13.0*t))))
    p2.set(1,0,256 + int(100.0*(1.5*sin(t) - sin(13.0*t))))
    window.drawLine(p1,p2,color)
window.saveImage("testImage.png")
window.showImage()