from math import *
import numpy as np
from matrix import matrix

class transform(matrix):

    def __init__(self):
        super().__init__(np.identity(4))

    def translate(self,Tx=0.0,Ty=0.0,Tz=0.0):
        self.set(0,3,Tx)
        self.set(1,3,Ty)
        self.set(2,3,Tz)
        return self

    def scale(self,Sx=1.0,Sy=1.0,Sz=1.0):
        self.set(0,0,Sx)
        self.set(1,1,Sy)
        self.set(2,2,Sz)
        return self

    def rotate(self,A=matrix(np.ones((3,1))),angle=0.0):
        A = A.normalize()
        V = matrix(np.zeros((4,4)))
        V.set(0,1,-A.get(2,0))
        V.set(0,2,A.get(1,0))
        V.set(1,0,A.get(2,0))
        V.set(1,2,-A.get(0,0))
        V.set(2,0,-A.get(1,0))
        V.set(2,1,A.get(0,0))
        return self + V.scalarMultiply(sin(angle)) + (V*V).scalarMultiply(1.0-cos(angle))