from PIL import Image

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    def drawLine(self,point1,point2,color):
        __exchange = False
        __inc1stCoord = 1
        __inc2ndCoord = 1
        __TransX = -int(point1.get(0,0))
        __TransY = -int(point1.get(1,0))
        __x1 = 0
        __y1 = 0
        __x2 = int(point2.get(0,0)) + __TransX
        __y2 = int(point2.get(1,0)) + __TransY
        __Dx = __x2
        __Dy = __y2
        __twoDx = 2*__x2
        __twoDy = 2*__y2
        if __Dy < 0:
            __inc2ndCoord = -1
            __Dy *= -1
            __twoDy *= -1
        if __Dx < 0:
            __inc1stCoord = -1
            __Dx *= -1
            __twoDx *= -1
        if __Dy > __Dx:
            __exchange = True
            __twoDx, __twoDy = __twoDy, __twoDx
            __Dx, __Dy, = __Dy, __Dx
            __inc1stCoord, __inc2ndCoord = __inc2ndCoord, __inc1stCoord
        __Pi = __twoDy - __Dx
        if __exchange:
            self.drawPoint((__y1-__TransX,__x1-__TransY),color)
        else:
            self.drawPoint((__x1-__TransX,__y1-__TransY),color)
        for i in range(__Dx):
            if __Pi < 0:
                __Pi += __twoDy
            else:
                __Pi += __twoDy - __twoDx
                __y1 += __inc2ndCoord
            __x1 += __inc1stCoord
            if __exchange:
                self.drawPoint((__y1-__TransX,__x1-__TransY),color)
            else:
                self.drawPoint((__x1-__TransX,__y1-__TransY),color)

    def drawSegments(self,segList,color):
        for __seg in segList:
            self.drawLine(__seg[0],__seg[1],color)

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height