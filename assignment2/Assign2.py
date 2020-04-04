from math import *
import numpy as np
from matrix import matrix
from graphicsWindow import graphicsWindow
from cameraMatrix import cameraMatrix
from parametricPlane import parametricPlane
from parametricCircle import parametricCircle
from parametricSphere import parametricSphere
from parametricTorus import parametricTorus
from parametricCone import parametricCone
from parametricCylinder import parametricCylinder
from wireMesh import wireMesh

#Set up constants required for the camera and the rendering process
#Near and far planes
NP = 10.0
FP = 50.0

#Image size
WIDTH = 2800
HEIGHT = 1600

#Image aspect
THETA = 45.0
ASPECT = WIDTH/HEIGHT

#Vector in the up direction
Px = 0.0
Py = 0.0
Pz = 1.0

#Position of camera
Ex = 40.0
Ey = 40.0
Ez = 85.0

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

#Set up the viewing point
E.set(0,0,Ex)
E.set(1,0,Ey)
E.set(2,0,Ez)

#Set up the gaze point
G.set(0,0,Gx)
G.set(1,0,Gy)
G.set(2,0,Gz)

#Plane attributes
planeT = matrix(np.identity(4))
planeT.set(0,3,0.0)
planeT.set(1,3,-50.0)
planeCol = (255,255,0)
planeRef = (0.0,0.0,0.0)
planeWidth = 20.0
planeLength = 20.0

#Circle attributes
circleT = matrix(np.identity(4))
circleT.set(0,3,-40.0)
circleT.set(1,3,40.0)
circleCol = (0,255,255)
circleRef = (0.0,0.0,0.0)
circleRadius = 10.0

#Sphere attributes
sphereT = matrix(np.identity(4))
sphereCol = (255,0,0)
sphereRef = (0.0,0.0,0.0)
sphereRadius = 10.0

#Torus attributes
torusT = matrix(np.identity(4))
torusCol = (0,255,0)
torusRef = (0.0,0.0,0.0)
torusInnerRadius = 20.0
torusOuterRadius = 5.0

#Cone attributes
coneT = matrix(np.identity(4))
coneT.set(0,3,-40.0)
coneT.set(1,3,0.0)
coneCol = (0,0,255)
coneRef = (0.0,0.0,0.0)
coneHeight = 20.0
coneRadius = 10.0

#Cylinder attributes
cylinderT = matrix(np.identity(4))
cylinderT.set(0,3,40.0)
cylinderT.set(1,3,0.0)
cylinderCol = (255,0,255)
cylinderRef = (0.0,0.0,0.0)
cylinderHeight = 20.0
cylinderRadius = 10.0

window = graphicsWindow(WIDTH,HEIGHT) #Open a graphics window
camera = cameraMatrix(P,E,G,NP,FP,WIDTH,HEIGHT,THETA) #Set camera viewing system

plane = parametricPlane(planeT,planeWidth,planeLength,planeCol,planeRef,(0.0,1.0),(0.0,1.0),(1.0/10.0,1.0/10.0))
circle = parametricCircle(circleT,circleRadius,circleCol,circleRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))
sphere = parametricSphere(sphereT,sphereRadius,sphereCol,sphereRef,(0.0,2.0*pi),(0.0,pi),(pi/18.0,pi/18.0))
cone = parametricCone(coneT,coneHeight,coneRadius,coneCol,coneRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))
cylinder = parametricCylinder(cylinderT,cylinderHeight,cylinderRadius,cylinderCol,cylinderRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))
torus = parametricTorus(torusT,torusInnerRadius,torusOuterRadius,torusCol,torusRef,(0.0,2.0*pi),(0.0,2.0*pi),(pi/18.0,pi/9.0))

window.drawSegments(wireMesh(plane,camera).getSegList(),planeCol)
window.drawSegments(wireMesh(circle,camera).getSegList(),circleCol)
window.drawSegments(wireMesh(sphere,camera).getSegList(),sphereCol)
window.drawSegments(wireMesh(cone,camera).getSegList(),coneCol)
window.drawSegments(wireMesh(cylinder,camera).getSegList(),cylinderCol)
window.drawSegments(wireMesh(torus,camera).getSegList(),torusCol)

window.saveImage("testImage.png")
window.showImage()