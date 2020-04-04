from math import *

class quadraticSolver:

    def __init__(self,a,b,c):
        self.__r = []
        discriminant = b*b - a*c
        if discriminant == 0.0:
            self.__r.append(-b/a)
        elif discriminant > 0.0:
            self.__r.extend([-b/a-sqrt(discriminant)/a,-b/a+sqrt(discriminant)/a])

    def getRoot(self):
        if self.__r != [] and min(self.__r) > 0.0:
            return min(self.__r)
        else:
            return -1.0