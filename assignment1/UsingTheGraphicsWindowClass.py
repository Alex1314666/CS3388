from graphicsWindow import graphicsWindow

#Create an image
window = graphicsWindow()

#For all the pixels in the image
for i in range(window.getWidth()):
    for j in range(window.getHeight()):
        window.drawPixel((i,j),(i%256,j%256,(i+j)%256)) #Write the color tupe to pixel tuple in image
window.saveImage("testImage.png") #Save the resulting image