import operator
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
        exchange = False
        inc1stCoord = 1
        inc2ndCoord = 1
        TransX = -int(point1.get(0,0))
        TransY = -int(point1.get(1,0))
        x1 = 0
        y1 = 0
        x2 = int(point2.get(0,0)) + TransX
        y2 = int(point2.get(1,0)) + TransY
        Dx = x2
        Dy = y2
        twoDx = 2*x2
        twoDy = 2*y2
        if Dy < 0:
            inc2ndCoord = -1
            Dy *= -1
            twoDy *= -1
        if Dx < 0:
            inc1stCoord = -1
            Dx *= -1
            twoDx *= -1
        if Dy > Dx:
            exchange = True
            twoDx, twoDy = twoDy, twoDx
            Dx, Dy, = Dy, Dx
            inc1stCoord, inc2ndCoord = inc2ndCoord, inc1stCoord
        Pi = twoDy - Dx
        if exchange: self.drawPoint((y1-TransX,x1-TransY),color)
        else: self.drawPoint((x1-TransX,y1-TransY),color)
        for i in range(Dx):
            if Pi < 0: Pi += twoDy
            else:
                Pi += twoDy - twoDx
                y1 += inc2ndCoord
            x1 += inc1stCoord
            if exchange: self.drawPoint((y1-TransX,x1-TransY),color)
            else: self.drawPoint((x1-TransX,y1-TransY),color)

    def fillPolygon(self,pointList,color):
        n = len(pointList)
        active = [False]*n
        horizontal = [False]*n
        #Find minimum and maximum y-coordinates among points in list
        minY = int(pointList[0].get(1,0))
        maxY = int(pointList[0].get(1,0))
        for point in pointList:
            if point.get(1,0) < minY:
                minY = int(point.get(1,0))
            if point.get(1,0) > maxY:
                maxY = int(point.get(1,0))
        #Find horizontal lines
        for i in range(n):
            horizontal[i] = int(pointList[i].get(1,0)) == int(pointList[(i+1)%n].get(1,0))
        #Find intersections with scan line
        for y in range(minY,maxY):
            intersections = []
            for i in range(n):
                if not horizontal[i]:
                    active[i] = int(pointList[i].get(1,0)) <= y <= int(pointList[(i+1)%n].get(1,0)) or  int(pointList[i].get(1,0)) >= y >= int(pointList[(i+1)%n].get(1,0))
            for i in range(n):
                if active[i] and not horizontal[i]:
                    if int(pointList[i].get(0,0)) == int(pointList[(i+1)%n].get(0,0)): #Vertical line
                        intersections.append(int(pointList[i].get(0,0)))
                    else:
                        m = (int(pointList[(i+1)%n].get(1,0)) - int(pointList[i].get(1,0)))/(int(pointList[(i+1)%n].get(0,0)) - int(pointList[i].get(0,0)))
                        b = int(pointList[i].get(1,0)) - m*int(pointList[i].get(0,0))
                        intersections.append(int(round((y-b)/m)))
            intersections.sort()
            #Draw from minimum intesection to maximum intersection
            for i in range(intersections[0],intersections[-1]+1):
                self.drawPoint((i,y),color)

    def drawFaces(self,faceList):
        faceList.sort(key = operator.itemgetter(0),reverse=True)
        for face in faceList:
            self.fillPolygon(face[1],face[2])

    def drawWireMesh(self,faceList):
        faceList.sort(key = operator.itemgetter(0),reverse=True)
        for face in faceList:
            self.drawPolygon(face[1],face[2])

    def drawPolygon(self,pointList,color):
        for i in range(len(pointList)-1):
            self.drawLine(pointList[i],pointList[i+1],color)
        self.drawLine(pointList[-1],pointList[0],color)

    def drawPolyline(self,pointList,color):
        for i in range(len(pointList)-1):
            self.drawLine(pointList[i],pointList[i+1],color)

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height