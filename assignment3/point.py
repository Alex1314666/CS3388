import numpy as np
from matrix import matrix

class point(matrix):

    def __init__(self,x=0.0,y=0.0,z=0.0,homogeneous=True):
        if homogeneous:
            super().__init__(np.ones((4,1)))
        else:
            super().__init__(np.ones((3,1)))
        self.set(0,0,x)
        self.set(1,0,y)
        self.set(2,0,z)