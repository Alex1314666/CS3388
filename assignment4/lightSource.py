import numpy as np
from matrix import matrix

class lightSource:

    def __init__(self,position=matrix(np.zeros((4,1))),color=(0,0,0),intensity=(1.0,1.0,1.0)):
        self.__position = position
        self.__color = color
        self.__intensity = intensity

    def getPosition(self):
        return self.__position

    def getColor(self):
        return self.__color

    def getIntensity(self):
        return self.__intensity

    def setPosition(self,position):
        self.__position = position

    def setColor(self,color):
        self.__color = color

    def setIntensity(self,intensity):
        self.__intensity = intensity