import numpy as np
from matrix import matrix

class tessel:

    def __init__(self,objectList,camera,light):
        self.__faceList = [] #List of faces with normals
        EPSILON = 0.001
        facePoints = [] #List of points for a face
        Lv = camera.worldToViewingCoordinates(light.getPosition()) #Transform light into viewing coordinates
        Li = light.getIntensity() #Obtain light intensity
        for object in objectList:
            c = object.getColor() #Obtain object color
            u = object.getURange()[0]
            while u + object.getUVDelta()[0] < object.getURange()[1]  + EPSILON:
                v = object.getVRange()[0]
                while v + object.getUVDelta()[1] < object.getVRange()[1] + EPSILON:
                    #Collect surface points transformed into viewing coordinates
                    facePoints.append(camera.worldToViewingCoordinates(object.getT()*object.getPoint(u,v)))
                    facePoints.append(camera.worldToViewingCoordinates(object.getT()*object.getPoint(u,v+object.getUVDelta()[1])))
                    facePoints.append(camera.worldToViewingCoordinates(object.getT()*object.getPoint(u+object.getUVDelta()[0],v+object.getUVDelta()[1])))
                    facePoints.append(camera.worldToViewingCoordinates(object.getT()*object.getPoint(u+object.getUVDelta()[0],v)))
                    #Do not render any surface behind the near plane
                    if not self.__minCoordinate(facePoints,2) > -camera.getNp():
                        C = self.__centroid(facePoints) #Find centroid point of face
                        N = self.__vectorNormal(facePoints) #Find normal vector to face
                        #Compute face shading. Do not include back faces
                        if not self.__backFace(C,N):
                            S = self.__vectorToLightSource(Lv,C)  # Find vector from centroid to light source
                            R = self.__vectorSpecular(S,N)  # Find specular reflection vector
                            V = self.__vectorToEye(C)  # Find vector from origin of viewing coordinates to surface centroid
                            index = self.__colorIndex(object,N,S,R,V)
                            faceColor = (int(c[0]*Li[0]*index),int(c[1]*Li[1]*index),int(c[2]*Li[2]*index))
                            #Transform 3D points expressed in viewing coordinates into 2D pixel coordinates
                            pixelFacePoints = []
                            for point in facePoints:
                                pixelFacePoints.append(camera.viewingToPixelCoordinates(point))
                            #Add face attributes to faceList with pseudo-depth
                            self.__faceList.append((camera.viewingToPixelCoordinates(C).get(2,0),pixelFacePoints,faceColor))
                    facePoints = []
                    v += object.getUVDelta()[1]
                u += object.getUVDelta()[0]

    def __minCoordinate(self,facePoints,coord):
        min = facePoints[0].get(coord,0)
        for point in facePoints:
            if point.get(coord,0) < min:
                min = point.get(coord,0)
        return min

    def __backFace(self,C,N):
        return C.dotProduct(N) > 0.0

    def __centroid(self,facePoints):
        sum = matrix(np.zeros((4,1)))
        for point in facePoints:
            sum += point
        return sum.scalarMultiply(1.0/float(len(facePoints)))

    def __vectorNormal(self,facePoints):
        U = (facePoints[3] - facePoints[1]).removeRow(3).normalize()
        V = (facePoints[2] - facePoints[0]).removeRow(3).normalize()
        return U.crossProduct(V).normalize().insertRow(3,0.0)

    def __vectorToLightSource(self,L,C):
        return (L.removeRow(3) - C.removeRow(3)).normalize().insertRow(3,0.0)

    def __vectorSpecular(self,S,N):
        return  S.scalarMultiply(-1.0) + N.scalarMultiply(2.0*(S.dotProduct(N)))

    def __vectorToEye(self,C):
        return C.removeRow(3).scalarMultiply(-1.0).normalize().insertRow(3,0.0)

    def __colorIndex(self,object,N,S,R,V):
        Id = (N.transpose()*S).get(0,0) #Compute local components of shading
        Is = (R.transpose()*V).get(0,0)
        if Id < 0.0: Id = 0.0
        if Is < 0.0: Is = 0.0
        r = object.getReflectance()
        index = r[0] + r[1]*Id + r[2]*Is**r[3]
        return index

    def getFaceList(self):
        return self.__faceList