from math import *
from vector import vector
from point import point
from graphicsWindow import graphicsWindow
from cameraMatrix import cameraMatrix
from lightSource import lightSource
from transform import transform
from parametricPlane import parametricPlane
from parametricCircle import parametricCircle
from parametricSphere import parametricSphere
from parametricTorus import parametricTorus
from parametricCone import parametricCone
from parametricCylinder import parametricCylinder
from tessel import tessel

NP = 10.0 #Near plane
FP = 200.0 #Far plane

WIDTH = 1400
HEIGHT = 800
THETA = 45.0

P = vector(0.0,0.0,1.0) #Vector in the up direction
E = point(120.0,120.0,40.0) #Set the camera position
G = point(0.0,0.0,-40.0) #Set the gaze point
L = point(10.0,10.0,40.0) #Set the light position

C = (1.0,1.0,1.0) #Light color
I = (1.0,1.0,1.0) #Light intensity

#Create and position a plane
planeT = transform().translate(-40.0,-40.0,-40.0)
planeCol = (255,0,255)
planeRef = (0.2,0.4,0.4,10.0)
planeWidth = 100.0
planeLength = 100.0
plane = parametricPlane(planeT,planeWidth,planeLength,planeCol,planeRef,(0.0,1.0),(0.0,1.0),(1.0/10.0,1.0/10.0))

#Create and position a cone
coneT = transform().translate(Tx=50.0)
coneCol = (0,255,0)
coneRef = (0.2,0.4,0.4,10.0)
coneHeight = 20.0
coneRadius = 10.0
cone = parametricCone(coneT,coneHeight,coneRadius,coneCol,coneRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))

#Create and position a sphere
sphereT = transform().translate(Tx=30.0)
sphereCol = (255,255,0)
sphereRef = (0.2,0.4,0.4,10.0)
sphereRadius = 10.0
sphere = parametricSphere(sphereT,sphereRadius,sphereCol,sphereRef,(0.0,pi),(0.0,2.0*pi),(pi/64.0,2.0*pi/64.0))

#Create and position a cylinder
cylinderT = transform().translate()
cylinderCol = (255,0,0)
cylinderRef = (0.2,0.4,0.4,10.0)
cylinderHeight = 20.0
cylinderRadius = 10.0
cylinder = parametricCylinder(cylinderT,cylinderHeight,cylinderRadius,cylinderCol,cylinderRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))

#Create and position a cylinder top cap
topCircleT = transform().translate(Tz=20.0) #Elevate to height of cylinder
topCircleCol = (255,0,0)
topCircleRef = (0.2,0.4,0.4,10.0)
topCircleRadius = 10.0
topCircle = parametricCircle(topCircleT,topCircleRadius,topCircleCol,topCircleRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))

#Create and position a cylinder bottom cap
bottomCircleT = transform().translate()
bottomCircleCol = (255,0,0)
bottomCircleRef = (0.2,0.4,0.4,10.0)
bottomCircleRadius = 10.0
bottomCircle = parametricCircle(bottomCircleT,bottomCircleRadius,bottomCircleCol,bottomCircleRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))

#Create and position a torus
torusT = transform().translate(Tx=25.0,Ty=25.0)
torusCol = (0,255,0)
torusRef = (0.2,0.4,0.4,10.0)
torusInnerRadius = 20.0
torusOuterRadius = 5.0
torus = parametricTorus(torusT,torusInnerRadius,torusOuterRadius,torusCol,torusRef,(0.0,2.0*pi),(0.0,2.0*pi),(2.0*pi/256.0,2.0*pi/64.0))

V = vector(1.0,1.0,1.0) #Set the rotation matrix for cylinder, its top, and its bottom caps
R1 = transform().rotate(V,pi/4.0)
V = vector(1.0,0.0,0.0) #Rotate the bottom circle by 180 degrees such that the normal points in the right direction
R2 = transform().rotate(V,pi)

#Apply transformations to objects in the correct order
cylinder.setT(R1*cylinder.getT())
bottomCircle.setT(R1*R2*bottomCircle.getT())
topCircle.setT(R1*topCircle.getT())

#Rotate the torus with the same rotation used for the cylinder
torus.setT(R1*torus.getT())

#Open a graphics window, set camera viewing system, and create light source
window = graphicsWindow(WIDTH,HEIGHT)
camera = cameraMatrix(window,P,E,G,NP,FP,THETA) #Set camera viewing system
light = lightSource(L,C,I)

#Draw the list of faces for the scene
window.drawFaces(tessel([cylinder,topCircle,bottomCircle,sphere,cone,torus,plane],camera,light).getFaceList())
window.saveImage("testImage.png")
window.showImage()