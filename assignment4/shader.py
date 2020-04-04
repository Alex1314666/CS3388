# author: Alex1314666
# date: 2020.04.03
class shader:
    # object is that which there is an intersection with
    # I is the intersection point
    # S is the vector to the light source
    # objectList is a list of objects composing the scene
    # Returns true if the ray from the intersection point to the light source intersects with an object from the scene
    # returns false otherwise
    def __shadowed(self,object,I,S,objectList):
        # matrix = matrix T associated with object
        matrix = object.getT()
        # compute I = matrix * (I + C- S) where c- = 0.001
        # This operation detaches the intersection point from its surface
        # and then transform it into world coordinates
        I = matrix * (I + S.scalarMultiply(0.001))
        # compute S = M * S
        # This transforms S into world coordinates
        S = matrix * S
        for k in objectList:
            matrixInverse = k.getTinv()
            # compute I = matrixInverse * I
            # This transforms the intersection point into the generic coordinates of the object
            Ik = matrixInverse * I
            # compute S = matrixInverse * S and nomalize S.
            # This transfomrs the vector to the light source into the generic coordinates of the object
            Sk = (matrixInverse * S).normalize()
            # if object. intersection (I,S) != -1.0
            # this means there is an intersection with another object
            if k.intersection(Ik,Sk) != -1.0:
                # return true
                return True
        # otherwise, return false
        return False

    # intersection is the first(K, t0) tuple from the intersection list
    # direction is the vector describing the direction of the ray
    # ObjectList is a list of objects composing the scene
    # and light is a lightSource object
    def __init__(self,intersection,direction,camera,objectList,light):
	#Complete this method
        # consider tuple (k,t0) from intersection
        self.__k = intersection[0]
        self.__object = objectList[objectList.index(self.__k)]
        #self.__object = objectList[self.__k]
        # t0 is the t-value associated with object from tuple (k,to)
        self.__t0 = intersection[1]
        # matrix Inverse  = inverse of matrix T associated with object
        self.__matrixInverse = self.__object.getT().inverse()
        # Ts = light position transformed with matrix reverse
        self.__Ts = self.__matrixInverse * light.getPosition()
        # Transform the ray with matrix reverse in the following way
        # Te = matrix reverse * e
        # where e is the position of the camera
        self.__Te = self.__matrixInverse * camera.getE()
        # Td = matrix reverse * d
        # where d is the direction of the ray
        self.__Td = self.__matrixInverse * direction
        # compute the intersection point as I = Te + Td * t0
        self.__I = self.__Te + self.__Td.scalarMultiply(self.__t0)
        # compute vector from intersection point to light source position as S = (Ts - I) and normalize it
        self.__S = (self.__Ts - self.__I).normalize()
        # compute normal vector at intersection point as N = object.normalVector(I)
        self.__N = self.__object.normalVector(self.__I)
        # compute specular reflection vector as R = -s + (2 * S * N) * N
        self.__R = self.__N.scalarMultiply(2 * (self.__S.removeRow(3).transpose() * self.__N.removeRow(3)).get(0,0)) - self.__S
        # compute vector to centyer of projection V = Te - I
        self.__V = (self.__Te - self.__I).normalize()
        # comput Id = max{N * S, 0} and Ix = max{R * V ,0}
        self.__Id = max(((self.__N.removeRow(3).transpose() * self.__S.removeRow(3)).get(0,0)), 0 )
        self.__Is = max(((self.__R.removeRow(3).transpose() * self.__V.removeRow(3)).get(0,0)), 0)
        # r = object.getReflectance()
        self.__r = self.__object.getReflectance()
        # c = object.getColor()
        self.__c = self.__object.getColor()
        # Li = light.getIntensity()
        self.__Li = light.getIntensity()
        self.__f = 0.0
        self.__color = (0,0,0)

        # if the intersection point is shadowed by objects, compute f = r[0]
        if self.__shadowed(self.__object, self.__I,self.__S,objectList):
            self.__f = self.__r[0]
        # if not comput f = r[0] + r[1]* Id + r[2] * Is ** r[3]
        else:
            self.__f = self.__r[0] + self.__r[1] * self.__Id + self.__r[2] * (self.__Is ** self.__r[3])
        # compute tuple self.__color = (f(c[0]Li[0],c[1]Li[1],c[2]Li[2]))
        #print((int(self.__f * self.__c[0] * self.__Li[0]), int(self.__f * self.__c[1] * self.__Li[1]), int(self.__f * self.__c[2] * self.__Li[2])))
        self.__color = (int(self.__f * self.__c[0] * self.__Li[0]), int(self.__f * self.__c[1] * self.__Li[1]), int(self.__f * self.__c[2] * self.__Li[2]))

    def getShade(self):
        return self.__color
