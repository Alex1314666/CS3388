class wireMesh:

    def __init__(self,objectList,camera):
        self.__faceList = []  # List of faces with normals
        EPSILON = 0.001
        facePoints = []  # List of points for a face
        for object in objectList:
            c = object.getColor()  # Obtain object color
            u = object.getURange()[0]
            while u + object.getUVDelta()[0] < object.getURange()[1] + EPSILON:
                v = object.getVRange()[0]
                while v + object.getUVDelta()[1] < object.getVRange()[1] + EPSILON:
                    # Collect surface points transformed into viewing coordinates
                    facePoints.append(camera.worldToPixelCoordinates(object.getT()*object.getPoint(u,v)))
                    facePoints.append(camera.worldToPixelCoordinates(object.getT()*object.getPoint(u,v+object.getUVDelta()[1])))
                    facePoints.append(camera.worldToPixelCoordinates(object.getT()*object.getPoint(u+object.getUVDelta()[0],v+object.getUVDelta()[1])))
                    facePoints.append(camera.worldToPixelCoordinates(object.getT()*object.getPoint(u+object.getUVDelta()[0],v)))
                    self.__faceList.append((0.0,facePoints,c))
                    facePoints = []
                    v += object.getUVDelta()[1]
                u += object.getUVDelta()[0]

    def getFaceList(self):
        return self.__faceList