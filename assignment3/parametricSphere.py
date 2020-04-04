from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricSphere(parametricObject):

    def __init__(self,T=matrix(np.identity(4)),radius=10.0,color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0),uRange=(0.0,pi),vRange=(0.0,2.0*pi),uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__radius = radius

    def getPoint(self,u,v):
        P = matrix(np.ones((4,1)))
        P.set(0,0,self.__radius*cos(v)*sin(u))
        P.set(1,0,self.__radius*sin(v)*sin(u))
        P.set(2,0,self.__radius*cos(u))
        return P

    def setRadius(self,radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius