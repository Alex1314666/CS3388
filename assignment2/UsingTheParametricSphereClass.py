from math import *
import numpy as np
from matrix import matrix
from parametricSphere import parametricSphere

sphere = parametricSphere(matrix(np.identity(4)),1.0,(255,255,255),(0.0,0.0,0.0),(0.0,2.0*pi),(0.0,pi),(0.1,0.1))