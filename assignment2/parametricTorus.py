from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricTorus(parametricObject):

    def __init__(self,T=matrix(np.identity(4)),innerRadius=1.0,outerRadius=2.0,color=(0,0,0),reflectance=(0.0,0.0,0.0),uRange=(0.0,0.0),vRange=(0.0,0.0),uvDelta=(0.0,0.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__innerRadius = innerRadius
        self.__outerRadius = outerRadius

    def getPoint(self,u,v):
        __P = matrix(np.ones((4,1)))
        __P.set(0,0,(self.__innerRadius+self.__outerRadius*cos(v))*cos(u))
        __P.set(1,0,(self.__innerRadius+self.__outerRadius*cos(v))*sin(u))
        __P.set(2,0,self.__outerRadius*sin(v))
        return __P

    def setInnerRadius(self,innerRadius):
        self.__innerRradius = innerRadius

    def setOuterRadius(self,outerRadius):
        self.__outerRadius = outerRadius

    def getInnerRadius(self):
        return self.__innerRadius

    def getOuterRadius(self):
        return self.__outerRadius