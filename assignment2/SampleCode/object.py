import numpy as np
from matrix import matrix

class object:

    def __init__(self,T=matrix(np.identity(4)),color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0)):
        self.__T = T
        self.__color = color
        self.__reflectance = reflectance

    def getT(self):
        return self.__T

    def getColor(self):
        return self.__color

    def getReflectance(self):
        return self.__reflectance

    def setT(self,T):
        self.__T = T

    def setColor(self,color):
        self.__color = color

    def setReflectance(self,reflectance):
        self.__reflectance = reflectance