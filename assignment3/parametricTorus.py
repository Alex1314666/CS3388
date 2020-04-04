from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricTorus(parametricObject):

    def __init__(self,T=matrix(np.identity(4)),innerRadius=10.0,outerRadius=5.0,color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0),uRange=(0.0,2.0*pi),vRange=(0.0,2.0*pi),uvDelta=(pi/18.0,pi/9.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__innerRadius = innerRadius
        self.__outerRadius = outerRadius

    def getPoint(self,u,v):
        P = matrix(np.ones((4,1)))
        P.set(0,0,(self.__innerRadius+self.__outerRadius*cos(v))*cos(u))
        P.set(1,0,(self.__innerRadius+self.__outerRadius*cos(v))*sin(u))
        P.set(2,0,self.__outerRadius*sin(v))
        return P

    def setInnerRadius(self,innerRadius):
        self.__innerRradius = innerRadius

    def setOuterRadius(self,outerRadius):
        self.__outerRadius = outerRadius

    def getInnerRadius(self):
        return self.__innerRadius

    def getOuterRadius(self):
        return self.__outerRadius