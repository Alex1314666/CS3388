import operator
from math import *
import numpy as np
from matrix import matrix
# author: Alex1314666
class cameraMatrix:

    def __init__(self,window,UP,E,G,nearPlane=10.0,farPlane=50.0,theta=90.0):
        self.__UP = UP.normalize()
        self.__E = E
        self.__G = G
        self.__np = nearPlane
        self.__fp = farPlane
        self.__width = window.getWidth()
        self.__height = window.getHeight()
        self.__theta = theta
        self.__aspect = self.__width/self.__height
        self.__npHeight = self.__np*(pi/180.0*self.__theta/2.0)
        self.__npWidth = self.__npHeight*self.__aspect

        Mp = self.__setMp(self.__np,farPlane)
        T1 = self.__setT1(self.__np,self.__theta,self.__aspect)
        S1 = self.__setS1(self.__np,self.__theta,self.__aspect)
        T2 = self.__setT2()
        S2 = self.__setS2(self.__width,self.__height)
        W2 = self.__setW2(self.__height)

        self.__N = (self.__E - self.__G).removeRow(3).normalize()
        self.__U = self.__UP.removeRow(3).crossProduct(self.__N).normalize()
        self.__V = self.__N.crossProduct(self.__U)

        self.__Mv = self.__setMv(self.__U,self.__V,self.__N,self.__E)
        self.__C = W2*S2*T2*S1*T1*Mp
        self.__M = self.__C*self.__Mv

    def __setMv(self,U,V,N,E):
        Mv = matrix(np.identity(4))
        Mv.set(0,0,U.get(0,0))
        Mv.set(0,1,U.get(1,0))
        Mv.set(0,2,U.get(2,0))
        Mv.set(0,3,-E.removeRow(3).dotProduct(U))

        Mv.set(1,0,V.get(0,0))
        Mv.set(1,1,V.get(1,0))
        Mv.set(1,2,V.get(2,0))
        Mv.set(1,3,-E.removeRow(3).dotProduct(V))

        Mv.set(2,0,N.get(0,0))
        Mv.set(2,1,N.get(1,0))
        Mv.set(2,2,N.get(2,0))
        Mv.set(2,3,-E.removeRow(3).dotProduct(N))
        return Mv

    def __setMp(self,nearPlane,farPlane):
        Mp = matrix(np.identity(4))
        Mp.set(0,0,nearPlane)
        Mp.set(1,1,nearPlane)
        Mp.set(2,2,-(farPlane+nearPlane)/(farPlane-nearPlane))
        Mp.set(2,3,-2.0*(farPlane*nearPlane)/(farPlane-nearPlane))
        Mp.set(3,2,-1.0)
        Mp.set(3,3,0.0)
        return Mp

    def __setT1(self,nearPlane,theta,aspect):
        top = nearPlane*tan(pi/180.0*theta/2.0)
        right = aspect*top
        bottom = -top
        left = -right
        T1 = matrix(np.identity(4))
        T1.set(0,3,-(right+left)/2.0)
        T1.set(1,3,-(top+bottom)/2.0)
        return T1

    def __setS1(self,nearPlane,theta,aspect):
        top = nearPlane*tan(pi/180.0*theta/2.0)
        right = aspect*top
        bottom = -top
        left = -right
        S1 = matrix(np.identity(4))
        S1.set(0,0,2.0/(right-left))
        S1.set(1,1,2.0/(top-bottom))
        return S1

    def __setT2(self):
        T2 = matrix(np.identity(4))
        T2.set(0,3,1.0)
        T2.set(1,3,1.0)
        return T2

    def __setS2(self,width,height):
        S2 = matrix(np.identity(4))
        S2.set(0,0,width/2.0)
        S2.set(1,1,height/2.0)
        return S2

    def __setW2(self,height):
        W2 = matrix(np.identity(4))
        W2.set(1,1,-1.0)
        W2.set(1,3,height)
        return W2

    def getRay(self,window,i,j):
        a = -self.__np
        b = self.__npWidth*(2.0*i/window.getWidth() - 1.0)
        c = self.__npHeight*(2.0*(window.getHeight() - (j+1))/window.getHeight() - 1.0)
        return (self.__N.scalarMultiply(a) + self.__U.scalarMultiply(b) + self.__V.scalarMultiply(c)).insertRow(3,0.0)

    # Direction is the vector describing the direction of the ray
    # objectList is a list of objects composing the scene
    def minimumIntersection(self,direction,objectList):
        # create empty intersection list
        intersectionList = []
        # for each object k in the list
        for k in objectList:
            # inverse of matrix T associated with object
            matrixInverse = k.getTinv()
            # transform the ray with M-inverse in the following way: Te = M-inverse*e, where e is the position of the camera
            # and Td = M-inverse*d, where d is the direction of the ray
            Te = matrixInverse * self.__E
            Td = matrixInverse * direction
            # t0 = object.intersection(Te,Td)
            t0 = k.intersection(Te,Td)
            # if t0 != -1.0 then add tuple (K,t0) to intersection list
            if t0 != -1.0:
                intersectionList.append((k,t0))
        # sort intersection list in increasing oder of t0
        intersectionList.sort(key = lambda tup:tup[1])
        # returns a list of tuples (k,t0) where k is the position in the list of an object that the ray intersects
        # t0 is the minimum t-value of the intersection the ray makes with the object
        # This list is sorted in increasing order of the t-values
        return intersectionList

    def worldToViewingCoordinates(self,P):
        return self.__Mv*P

    def worldToImageCoordinates(self,P):
        return self.__M*P

    def worldToPixelCoordinates(self,P):
        return self.__M*P.scalarMultiply(1.0/(self.__M*P).get(3,0))

    def viewingToImageCoordinates(self,P):
        return self.__C*P

    def viewingToPixelCoordinates(self,P):
        return self.__C*P.scalarMultiply(1.0/(self.__C*P).get(3,0))

    def imageToPixelCoordinates(self,P):
        return P.scalarMultiply(1.0/P.get(3,0))

    def getUP(self):
        return self.__UP

    def getU(self):
        return self.__U

    def getV(self):
        return self.__V

    def getN(self):
        return self.__N

    def getE(self):
        return self.__E

    def getG(self):
        return self.__G

    def getMv(self):
        return self.__Mv

    def getC(self):
        return self.__C

    def getM(self):
        return self.__M

    def getNp(self):
        return self.__np

    def getFp(self):
        return self.__fp

    def getTheta(self):
        return self.__theta

    def getAspect(self):
        return self.__aspect

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getNpHeight(self):
        return self.__npHeight

    def getNpWidth(self):
        return self.__npWidth
