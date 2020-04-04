import numpy as np

class matrix:

    def __init__(self,m):
        self.__r = m.shape[0]
        self.__c = m.shape[1]
        self.__m = m

    def set(self,r,c,a):
        self.__m[r][c] = a

    def get(self,r,c):
        return self.__m[r][c]

    def getNumberOfRows(self):
        return self.__r

    def getNumberOfColumns(self):
        return self.__c

    def initialize(self,a):
        return matrix(np.full((self.__r,self.__c),a))

    def scalarMultiply(self,a):
        return matrix(np.dot(self.__m,a))

    def norm(self):
        return np.linalg.norm(self.__m)

    def normalize(self):
        return self.scalarMultiply(1.0/self.norm())

    def transpose(self):
        return matrix(np.transpose(self.__m))

    def dotProduct(self,rhs):
        return matrix(np.dot(np.transpose(self.__m),rhs.__m)).get(0,0)

    def crossProduct(self,rhs):
        return matrix(np.cross(np.transpose(self.__m),np.transpose(rhs.__m))).transpose()

    def determinant(self):
        return np.linalg.det(self.__m)

    def inverse(self):
        return matrix(np.linalg.inv(self.__m))

    def __neg__(self):
        return matrix(np.negative(self.__m))

    def __eq__(self,rhs):
        return np.array_equal(self.__m,rhs.__m)

    def __add__(self,rhs):
        return matrix(np.add(self.__m,rhs.__m))

    def __sub__(self,rhs):
        return matrix(np.subtract(self.__m,rhs.__m))

    def __mul__(self,rhs):
        return matrix(np.dot(self.__m,rhs.__m))

    def removeRow(self,r):
        return matrix(np.delete(self.__m,r,0))

    def removeColumn(self,c):
        return matrix(np.delete(self.__m,c,1))

    def insertRow(self,r,a):
        return matrix(np.insert(self.__m,r,a,0))

    def insertColumn(self,c,a):
        return matrix(np.insert(self.__m,c,a,1))

    def copyMatrix(self):
        return matrix(np.copy(self.__m))

    def __repr__(self):
        outStr = ""
        for i in range(self.__r):
            for j in range(self.__c):
                outStr += str("%16.6f" % (self.__m[i][j]))
            outStr += "\n"
        return outStr