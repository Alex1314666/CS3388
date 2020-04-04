import numpy as np
from matrix import matrix
from object import object

class parametricObject(object):

    def __init__(self,T=matrix(np.identity(4)),color=(0,0,0),reflectance=(0.0,0.0,0.0),uRange=(0.0,0.0),vRange=(0.0,0.0),uvDelta=(0.0,0.0)):
        super().__init__(T,color,reflectance)
        self.__uRange = uRange
        self.__vRange = vRange
        self.__uvDelta = uvDelta

    def getURange(self):
        return self.__uRange

    def getVRange(self):
        return self.__vRange

    def getUVDelta(self):
        return self.__uvDelta

    def setURange(self,uRange):
        self.__uRange = uRange

    def setVRange(self,vRange):
        self.__vRange = vRange

    def setUVDelta(self,uvDelta):
        self.__uvDelta = uvDelta

