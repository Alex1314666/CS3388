from vector import vector
from point import point
from lightSource import lightSource
from transform import transform
from graphicsWindow import graphicsWindow
from cameraMatrix import cameraMatrix
from implicitSphere import implicitSphere
from shader import shader

NP = 1.0
FP = 25.0

WIDTH = 512
HEIGHT = 512
THETA = 45.0

P = vector(0.0,0.0,1.0) #Up vector
E = point(5.0,5.0,5.0) #Camera position
G = point(0.0,0.0,0.0) #Gaze point

L = point(5.0,0.0,3.0) #Set light position
C = (1.0,1.0,1.0) #Light color
I = (1.0,1.0,1.0) #Light intensity

light = lightSource(L,C,I)
window = graphicsWindow(WIDTH,HEIGHT)
camera = cameraMatrix(window,P,E,G,NP,FP,THETA)

#Creating a scene with three spheres
objectList = []
objectList.append(implicitSphere(color=(255,0,255),T=transform().translate(),reflectance=(0.2,0.4,0.4,10.0)))
objectList.append(implicitSphere(color=(0,255,0),T=transform().translate(Tx=-2.0,Tz=0.0),reflectance=(0.2,0.4,0.4,10.0)))
objectList.append(implicitSphere(color=(255,255,0),T=transform().translate(Tx=2.0,Tz=-0.0),reflectance=(0.2,0.4,0.4,10.0)))

for i in range(window.getWidth()):
    for j in range(window.getHeight()):
        direction = camera.getRay(window,i,j) #Compute ray direction
        iList = camera.minimumIntersection(direction,objectList) #Find minimum intersection time for ray
        #iList contains tuples (k,t0) where k is position of the object in the list
        #and t0 is the minimum intersection time, sorted in increasing values of t0
        if len(iList) > 0: #If we have an intersection, then set pixel (i,j) to color obtained with shader
            window.drawPoint((i,j),shader(iList[0],direction,camera,objectList,light).getShade())
window.saveImage("testImage.png")
window.showImage()