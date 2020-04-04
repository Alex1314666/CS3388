import numpy as np
from matrix import matrix
from quadraticSolver import quadraticSolver
from implicitObject import implicitObject

class implicitSphere(implicitObject):

    def __init__(self,T=matrix(np.identity(4)),radius=1.0,color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0)):
        super().__init__(T,color,reflectance)
        self.__radius = radius

    def intersection(self,e,d):
        e = e.removeRow(3)
        d = d.removeRow(3)
        return quadraticSolver(d.dotProduct(d),d.dotProduct(e),e.dotProduct(e)-1.0).getRoot()

    def normalVector(self,intersectionPoint):
        return intersectionPoint.removeRow(3).normalize().insertRow(3,0.0)

    def getRadius(self):
        return self.__radius