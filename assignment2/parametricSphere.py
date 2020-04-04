from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricSphere(parametricObject):

    def __init__(self,T=matrix(np.identity(4)),radius=1.0,color=(0,0,0),reflectance=(0.0,0.0,0.0),uRange=(0.0,0.0),vRange=(0.0,0.0),uvDelta=(0.0,0.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__radius = radius

    def getPoint(self,u,v):
        __P = matrix(np.ones((4,1)))
        __P.set(0,0,self.__radius*cos(u)*sin(v))
        __P.set(1,0,self.__radius*sin(u)*sin(v))
        __P.set(2,0,self.__radius*cos(v))
        return __P

    def setRadius(self,radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius