from math import *
from graphicsWindow import graphicsWindow

window = graphicsWindow(512,512)

t = 0.0
dt = 2.0*pi/200.0
color = (255,255,255)

while t < 2.0*pi:
    x1 = 256 + int(100.0*(1.5*cos(t) - cos(13.0*t)))
    y1 = 256 + int(100.0*(1.5*sin(t) - sin(13.0*t)))
    t += dt
    x2 = 256 + int(100.0*(1.5*cos(t) - cos(13.0*t)))
    y2 = 256 + int(100.0*(1.5*sin(t) - sin(13.0*t)))
    window.drawLine((x1,y1),(x2,y2),color)

window.saveImage("testImage.png")
