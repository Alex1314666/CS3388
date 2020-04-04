class wireMesh:

    def __init__(self,object,camera):
        __EPSILON = 0.001
        self.__segList = []
        __u = object.getURange()[0]

        while __u + object.getUVDelta()[0] < object.getURange()[1]  + __EPSILON:
            __v = object.getVRange()[0]

            while __v + object.getUVDelta()[1] < object.getVRange()[1] + __EPSILON:
                # Get object points in world coordinates, transform with object's transformation, and put into pixel coordinates
                __p1 = camera.worldToPixelCoordinates(object.getT()*object.getPoint(__u,__v))
                __p2 = camera.worldToPixelCoordinates(object.getT()*object.getPoint(__u+object.getUVDelta()[0],__v))
                __p3 = camera.worldToPixelCoordinates(object.getT()*object.getPoint(__u+object.getUVDelta()[0],__v+object.getUVDelta()[1]))
                __p4 = camera.worldToPixelCoordinates(object.getT()*object.getPoint(__u,__v+object.getUVDelta()[1]))

                self.__segList.append((__p1,__p2))
                self.__segList.append((__p2,__p3))
                self.__segList.append((__p3,__p4))
                self.__segList.append((__p4,__p1))

                __v += object.getUVDelta()[1]

            __u += object.getUVDelta()[0]

    def getSegList(self):
        return self.__segList