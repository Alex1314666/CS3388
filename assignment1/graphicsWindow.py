# author: Alex1314666
# date: 2020.01.24
from PIL import Image
import math

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def drawPixel(self,pixel,color):
        self.__image[pixel[0],pixel[1]] = color

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    # function for circle generation
    # Bresenham's algorithm

    def drawLine(self,p1,p2,color):
        # x1, y1, x2, y2 >0
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        # m = 0
        if abs(y2 - y1) == 0 or abs(x2 - x1) == 0:
            m = 0
            if x2 == x1:
                if y2 <= y1:
                    y1,y2 = y2,y1
                for y in range(y1,y2):
                    self.drawPixel((x1,y),color)
            elif y1 == y2:
                if x2 <=x1:
                    x1,x2 = x2,x1
                    y1,y2 = y2,y1
                for x in range(x1,x2):
                    self.drawPixel((x,y1),color)
        elif abs(y2 - y1) < abs(x2 - x1):
            # 0 < m < 1
            if (x2 - x1 != 0):
                m = (y2 - y1) / (x2 - x1)
                if( m > 0):
                    if (y2 < y1):
                        y1,y2 = y2,y1
                        x1,x2 = x2,x1
                    dy = y2 - y1
                    dx = x2 - x1
                    for x in range(x1,x2):
                        if (x == x1):
                           p = 2 * dy - dx
                           y = y1
                        else:
                            if p < 0:
                                p = p + 2 * dy
                            else:
                                p = p + 2 * dy - 2* dx
                                y += 1
                        self.drawPixel((x,y),color)
                # -1 < m < 0
                else:
                    if y2 > y1 and x2 < x1:
                        y1,y2 = y2,y1
                        x1,x2 = x2,x1
                    dy = y1 - y2
                    dx = x2 - x1
                    for x in range(x1,x2):
                        if x == x1:
                            p = 2 * dy - dx
                            y = y1
                        else:
                            if p < 0:
                                p = p + 2 * dy
                            else:
                                p = p + 2 * dy - 2* dx
                                y -= 1
                        self.drawPixel((x,y),color)
        else:
            # let line y = mx + c be x = 1/m * y -c
            if y2 - y1 != 0:
                m = (x2 - x1) / (y2 - y1)
                if m > 0:
                    if x2 < x1:
                        x1,x2 = x2,x1
                        y1,y2 = y2,y1
                    dy = y2 - y1
                    dx = x2 - x1
                    for y in range(y1,y2):
                        if y == y1:
                           p = 2 * dx - dy
                           x = x1
                        else:
                            if p < 0:
                                p = p + 2 * dx
                            else:
                                p = p + 2 * dx - 2* dy
                                x += 1
                        self.drawPixel((x,y),color)
                else:
                    if y2 < y1:
                        x1,x2 = x2,x1
                        y1,y2 = y2,y1
                    dy = y2- y1
                    dx = x1- x2
                    for y in range(y1,y2):
                        if y == y1:
                           p = 2 * dx - dy
                           x = x1
                        else:
                            if p < 0:
                                p = p + 2 * dx
                            else:
                                p = p + 2 * dx - 2* dy
                                x -= 1
                        self.drawPixel((x,y),color)
