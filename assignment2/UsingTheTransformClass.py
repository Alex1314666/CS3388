from math import *
import numpy as np
from matrix import matrix
from transform import transform

#Creating a translation matrix M
M1 = transform().translate(matrix(np.zeros((3,1))).initialize(10.0))
print(M1)

#Creating a scaling matrix M
M2 = transform().scale(matrix(np.zeros((3,1))).initialize(5.0))
print(M2)

#creating a rotation matrix M with angle pi/2.0 around axis V
M = transform().rotate(matrix(np.ones((3,1))),pi/2.0)
print(M)