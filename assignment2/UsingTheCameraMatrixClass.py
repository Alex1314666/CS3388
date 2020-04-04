import numpy as np
from matrix import matrix
from cameraMatrix import cameraMatrix

#Near and far planes
NP = 10.0
FP = 50.0

#Image size
WIDTH = 1400
HEIGHT = 800

#Image aspect
THETA = 90.0
ASPECT = WIDTH/HEIGHT

#Vector in the up direction
Px = 0.0
Py = 0.0
Pz = 1.0

#Position of camera
Ex = 20.0
Ey = 20.0
Ez = 40.0

#Gaze point
Gx = 0.0
Gy = 0.0
Gz = 0.0

P = matrix(np.ones((4,1)))
E = matrix(np.ones((4,1)))
G = matrix(np.ones((4,1)))

#Set up the up vector
P.set(0,0,Px)
P.set(1,0,Py)
P.set(2,0,Pz)

#Set up the viewing point vector
E.set(0,0,Ex)
E.set(1,0,Ey)
E.set(2,0,Ez)

#Set up the gaze direction
G.set(0,0,Gx)
G.set(1,0,Gy)
G.set(2,0,Gz)

#Set the camera
camera = cameraMatrix(P,E,G,NP,FP,WIDTH,HEIGHT,THETA)

#Set a world point (0,0,0,1)
worldPoint = matrix(np.zeros((4,1)))
worldPoint.set(0,0,0.0)
worldPoint.set(1,0,0.0)
worldPoint.set(2,0,0.0)
worldPoint.set(3,0,1.0)

#Obtain coordinates of world point in viewing coordinates
viewPoint = camera.worldToViewingCoordinates(worldPoint)
print(viewPoint)

#Obtain coordinates of viewing point in image coordinates
imagePoint = camera.viewingToImageCoordinates(viewPoint)
print(imagePoint)

#Obtain coordinates of image point in pixel coordinates
pixelPoint = camera.imageToPixelCoordinates(imagePoint)
print(pixelPoint)

#Obtain coordinate of world point in pixel coordinates
pixelPoint = camera.worldToPixelCoordinates(worldPoint)
print(pixelPoint)