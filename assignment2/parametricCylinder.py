from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCylinder(parametricObject):
    #inital
    def __init__(self,T=matrix(np.identity(4)),height=1.0,radius=1.0,color=(0,0,0),reflectance=(0.0,0.0,0.0),uRange=(0.0,0.0),vRange=(0.0,0.0),uvDelta=(0.0,0.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__radius = radius
        self.__height = height
    # get 3D point
    def getPoint(self,u,v):
        # create a 4*1 matrix with value 1
        __P = matrix(np.ones((4,1)))
        # set values
        __P.set(0,0, self.__radius * cos(v))
        __P.set(1,0, self.__radius * sin(v))
        __P.set(2,0, self.__height * u)
        # return P
        return __P
    # set radius
    def setRadius(self,radius):
        self.__radius = radius
    # return radius
    def getRadius(self):
        return self.__radius
    # return height
    def getHeight(self):
        return self.__height
    # set height
    def setHeight(self,height):
        self.__height = height
