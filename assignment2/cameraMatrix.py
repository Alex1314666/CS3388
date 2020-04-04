
import math
import numpy as np

from matrix import matrix

class cameraMatrix:

    def __init__(self,UP,E,G,nearPlane=10.0,farPlane=50.0,width=640,height=480,theta=90.0):
        __Mp = self.__setMp(nearPlane,farPlane)
        __T1 = self.__setT1(nearPlane,theta,width/height)
        __S1 = self.__setS1(nearPlane,theta,width/height)
        __T2 = self.__setT2()
        __S2 = self.__setS2(width,height)
        __W2 = self.__setW2(height)

        self.__UP = UP.normalize()
        self.__N = (E - G).removeRow(3).normalize()
        self.__U = self.__UP.removeRow(3).transpose().crossProduct(self.__N.transpose()).normalize().transpose()
        self.__V = self.__N.transpose().crossProduct(self.__U.transpose()).transpose()
        self.__Mv = self.__setMv(self.__U,self.__V,self.__N,E)
        self.__C = __W2*__S2*__T2*__S1*__T1*__Mp
        self.__M = self.__C*self.__Mv

    def __setMv(self,U,V,N,E):

        #Complete this method
        #create a 4*4 identity matrix
        __Mv = matrix(np.identity(4))
        #set first row
        __Mv.set(0,0,U.get(0,0))
        __Mv.set(0,1,U.get(1,0))
        __Mv.set(0,2,U.get(2,0))
        __Mv.set(0,3,-( E.get(0,0) * U.get(0,0) + E.get(1,0) * U.get(1,0) + E.get(2,0) * U.get(2,0)))
        #set second row
        __Mv.set(1,0,V.get(0,0))
        __Mv.set(1,1,V.get(1,0))
        __Mv.set(1,2,V.get(2,0))
        __Mv.set(1,3,-( E.get(0,0) * V.get(0,0) + E.get(1,0) * V.get(1,0) + E.get(2,0) * V.get(2,0)))
        #set third row
        __Mv.set(2,0,N.get(0,0))
        __Mv.set(2,1,N.get(1,0))
        __Mv.set(2,2,N.get(2,0))
        __Mv.set(2,3,-( E.get(0,0) * N.get(0,0) + E.get(1,0) * N.get(1,0) + E.get(2,0) * N.get(2,0)))
        #no need to set fourth row because it is already 0 0 0 1
        #return mv matrix
        return __Mv

    def __setMp(self,nearPlane,farPlane):

        #Complete the is method
        #create a 4*4 identity matrix
        __Mp = matrix(np.identity(4))
        #set values
        __Mp.set(0,0,nearPlane)
        __Mp.set(1,1,nearPlane)
        __Mp.set(2,2,-( nearPlane + farPlane ) / ( farPlane - nearPlane ))
        __Mp.set(2,3,-2 * (farPlane * nearPlane) / (farPlane - nearPlane))
        __Mp.set(3,2,-1)
        __Mp.set(3,3,0)
        # return mp
        return __Mp

    def __setT1(self,nearPlane,theta,aspect):
        # calculate top, right, bottom, left (t,r,b,l)
        top = nearPlane * math.tan(math.pi/180.0 * theta / 2.0)
        right = aspect * top
        bottom = -top
        left = -right
        #create a 4*4 identity matrix
        __T1 = matrix(np.identity(4))
        #set values
        __T1.set(0,3, -(right + left) / 2.0)
        __T1.set(1,3,-(top + bottom)/2.0)
        #return T1

        return __T1

    def __setS1(self,nearPlane,theta,aspect):
        # calculate top, right, bottom, left (t,r,b,l)
        top = nearPlane * math.tan(math.pi/180.0 * theta / 2.0)
        right = aspect * top
        bottom = -top
        left = -right
        #create a 4*4 identity matrix
        __S1 = matrix(np.identity(4))
        #set values
        __S1.set(0,0,2.0/(right - left))
        __S1.set(1,1,2.0/(top - bottom))
        #return S1
        return __S1

    def __setT2(self):
        #create a 4*4 identity matrix
        __T2 = matrix(np.identity(4))
        #set values
        __T2.set(0,3,1.0)
        __T2.set(1,3,1.0)
        #return T2
        return __T2

    def __setS2(self,width,height):
        #create a 4*4 identity matrix
        __S2 = matrix(np.identity(4))
        #set values
        __S2.set(0,0,width/2.0)
        __S2.set(1,1,height/2.0)
        #return s2
        return __S2

    def __setW2(self,height):
        
        #Complete this method
        #create a 4*4 identity matrix
        __W2 = matrix(np.identity(4))
        #set values
        __W2.set(1,1,-1.0)
        __W2.set(1,3, height)
        #return w2
        return __W2

    def worldToViewingCoordinates(self,P):
        return self.__Mv*P

    def viewingToImageCoordinates(self,P):
        return self.__C*P

    def imageToPixelCoordinates(self,P):
        return P.scalarMultiply(1.0/P.get(3,0))

    def worldToImageCoordinates(self,P):
        return self.__M*P

    def worldToPixelCoordinates(self,P):
        return self.__M*P.scalarMultiply(1.0/(self.__M*P).get(3,0))

    def getUP(self):
        return self.__UP

    def getU(self):
        return self.__U

    def getV(self):
        return self.__V

    def getN(self):
        return self.__N

    def getMv(self):
        return self.__Mv

    def getC(self):
        return self.__C

    def getM(self):
        return self.__M
