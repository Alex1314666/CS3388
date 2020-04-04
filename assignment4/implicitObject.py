import numpy as np
from matrix import matrix
from object import object


class implicitObject(object):

    def __init__(self,T=matrix(np.identity(4)),color=(0,0,0),reflectance=(0.0,0.0,0.0,0.0)):
        super().__init__(T,color,reflectance)
        self.__Tinv = T.inverse()

    def getTinv(self):
        return self.__Tinv

    def setTinv(self,M):
        self.__Tinv = M