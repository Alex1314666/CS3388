from math import *
from vector import vector
from point import point
from transform import transform
from graphicsWindow import graphicsWindow
from cameraMatrix import cameraMatrix
from parametricPlane import parametricPlane
from parametricCircle import parametricCircle
from parametricSphere import parametricSphere
from parametricTorus import parametricTorus
from parametricCone import parametricCone
from parametricCylinder import parametricCylinder
from wireMesh import wireMesh

NP = 10.0 #Near plane
FP = 200.0 #Far plane

WIDTH = 2800
HEIGHT = 1600
THETA = 45.0

P = vector(0.0,0.0,1.0) #Vector in the up direction
E = point(40.0,40.0,85.0) #Camera position
G = point(0.0,0.0,0.0) #Gaze point

#Plane attributes

planeT = transform().translate(Ty=-50.0)
planeCol = (255,255,0)
planeRef = (0.0,0.0,0.0,0.0)
planeWidth = 20.0
planeLength = 20.0

#Circle attributes
circleT = transform().translate(Tx=-40.0,Ty=40.0)
circleCol = (0,255,255)
circleRef = (0.0,0.0,0.0,0.0)
circleRadius = 10.0

#Sphere attributes
sphereT = transform().translate()
sphereCol = (255,0,0)
sphereRef = (0.0,0.0,0.0,0.0)
sphereRadius = 10.0

#Torus attributes
torusT = transform().translate()
torusCol = (0,255,0)
torusRef = (0.0,0.0,0.0,0.0)
torusInnerRadius = 20.0
torusOuterRadius = 5.0

#Cone attributes
coneT = transform().translate(Tx=-40.0)
coneCol = (0,0,255)
coneRef = (0.0,0.0,0.0,0.0)
coneHeight = 20.0
coneRadius = 10.0

#Cylinder attributes
cylinderT = transform().translate(Tx=40.0)
cylinderCol = (255,0,255)
cylinderRef = (0.0,0.0,0.0,0.0)
cylinderHeight = 20.0
cylinderRadius = 10.0

window = graphicsWindow(WIDTH,HEIGHT) #Open a graphics window
camera = cameraMatrix(window,P,E,G,NP,FP,THETA) #Set camera viewing system

plane = parametricPlane(planeT,planeWidth,planeLength,planeCol,planeRef,(0.0,1.0),(0.0,1.0),(1.0/10.0,1.0/10.0))
circle = parametricCircle(circleT,circleRadius,circleCol,circleRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))
sphere = parametricSphere(sphereT,sphereRadius,sphereCol,sphereRef,(0.0,2.0*pi),(0.0,pi),(pi/18.0,pi/18.0))
cone = parametricCone(coneT,coneHeight,coneRadius,coneCol,coneRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))
cylinder = parametricCylinder(cylinderT,cylinderHeight,cylinderRadius,cylinderCol,cylinderRef,(0.0,1.0),(0.0,2.0*pi),(1.0/10.0,pi/18.0))
torus = parametricTorus(torusT,torusInnerRadius,torusOuterRadius,torusCol,torusRef,(0.0,2.0*pi),(0.0,2.0*pi),(pi/18.0,pi/9.0))

window.drawWireMesh(wireMesh([plane,circle,sphere,cone,cylinder,torus],camera).getFaceList())
window.saveImage("testImage.png")
window.showImage()