import os
from datetime import *
from math import *
from vector import vector
from point import point
import numpy as np
from matrix import matrix
from graphicsWindow import graphicsWindow
from cameraMatrix import cameraMatrix
from lightSource import lightSource
from transform import transform
from parametricTorus import parametricTorus
from tessel import tessel

NP = 10.0 #Near plane
FP = 200.0 #Far plane

WIDTH = 1800
HEIGHT = 840
THETA = 45.0

P = vector(0.0,0.0,1.0) #Vector in the up direction
E = point(80.0,80.0,40.0) #Set the camera position
G = point(0.0,0.0,00.0) #Set the gaze point
L = point(0.0,0.0,40.0) #Set the light position

C = (1.0,1.0,1.0) #Light color
I = (1.0,1.0,1.0) #Light intensity

#Create and position three torii
torusT1 = transform().translate()
torusCol1 = (0,255,0)
torusRef1 = (0.2,0.4,0.4,10.0)
torusInnerRadius1 = 20.0
torusOuterRadius1 = 2.0
torus1 = parametricTorus(torusT1,torusInnerRadius1,torusOuterRadius1,torusCol1,torusRef1,(0.0,2.0*pi),(0.0,2.0*pi),(2.0*pi/256.0,2.0*pi/64.0))

torusT2 = transform().translate()
torusCol2 = (255,0,0)
torusRef2 = (0.2,0.4,0.4,10.0)
torusInnerRadius2 = 15.0
torusOuterRadius2 = 2.0
torus2 = parametricTorus(torusT2,torusInnerRadius2,torusOuterRadius2,torusCol2,torusRef2,(0.0,2.0*pi),(0.0,2.0*pi),(2.0*pi/256.0,2.0*pi/64.0))

torusT3 = transform().translate()
torusCol3 = (0,0,255)
torusRef3 = (0.2,0.4,0.4,10.0)
torusInnerRadius3 = 10.0
torusOuterRadius3 = 2.0
torus3 = parametricTorus(torusT3,torusInnerRadius3,torusOuterRadius3,torusCol3,torusRef3,(0.0,2.0*pi),(0.0,2.0*pi),(2.0*pi/256.0,2.0*pi/64.0))

theta = pi/64.0
R1 = transform().rotate(vector(1.0,0.0,0.0),theta)
R2 = transform().rotate(vector(0.0,1.0,0.0),theta)
R3 = transform().rotate(vector(1.0,1.0,0.0),theta)

#Produce movie
FRAMES = 64
d1 = datetime.now() #Measure the time required to produce the movie
light = lightSource(L,C,I) #Set light source position, color, and intensity
window = graphicsWindow(WIDTH,HEIGHT)  #Create frame
camera = cameraMatrix(window,P,E,G,NP,FP,THETA)  # Set camera viewing system

for i in range(FRAMES):
    print("Producing frame: ",i)
    torus1.setT(R1*torus1.getT())
    torus2.setT(R2*torus2.getT())
    torus3.setT(R3*torus3.getT())
    window.drawFaces(tessel([torus1,torus2,torus3],camera,light).getFaceList())
    window.saveImage("/Users/beau/Desktop/movie-1/image-" + str(i).zfill(3) + ".png")
    window = graphicsWindow(WIDTH,HEIGHT)  #Create frame

os.system("ffmpeg -y -loglevel 0 -framerate 24 -i /Users/beau/Desktop/movie-1/image-%3d.png -f mp4 -vcodec libx264 -pix_fmt yuv420p /Users/beau/Desktop/movie-1/test.mp4")
d2 = datetime.now()
print("Time elapsed: ",d2-d1)