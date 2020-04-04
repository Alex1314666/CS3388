from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricPlane(parametricObject):
    # initial
    def __init__(self,T=matrix(np.identity(4)),width=1.0,length=1.0,color=(0,0,0),reflectance=(0.0,0.0,0.0),uRange=(0.0,0.0),vRange=(0.0,0.0),uvDelta=(0.0,0.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__width = width
        self.__length = length

    # get 3D point
    def getPoint(self,u,v):
        # create a 4*1 matrix with value 1
        __P = matrix(np.ones((4,1)))
        #set values
        __P.set(0,0, self.__width * u)
        __P.set(1,0, self.__length * v)
        __P.set(2,0, 0)
        #return points
        return __P

    # set width method
    def setWidth(self,width):
        self.__width = width
    # set length method
    def setLength(self,length):
        self.__length = length
    # return width
    def getWidth(self):
        return self.__width
    # return length
    def getLength(self):
        return self.__length
