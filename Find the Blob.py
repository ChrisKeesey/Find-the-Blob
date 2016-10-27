import Myro
from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 150 and getGreen(pixel) < 50 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel) < 50 and getGreen(pixel) > 100 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) < 50 and getGreen(pixel) < 50  and getBlue(pixel) > 150):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 200 and getGreen(pixel) > 150 and getBlue(pixel) < 50):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################
def changecolor(a,b,c,d,e):
    poly = Circle((50, 50), e)
    poly.bodyType = "static"
    poly.color = Color(a)
    poly.outline = Color("black")
    sim.addShape(poly)
    poly = Circle((50, 450), e)
    poly.bodyType = "static"
    poly.color = Color(b)
    poly.outline = Color("black")
    sim.addShape(poly)
    poly = Circle((450, 450), e)
    poly.bodyType = "static"
    poly.color = Color(c)
    poly.outline = Color("black")
    sim.addShape(poly)
    poly = Circle((450, 50), e)
    poly.bodyType = "static"
    poly.color = Color(d)
    poly.outline = Color("black")
    sim.addShape(poly)


def nextcolor1():
    backward(2.5,2)
    changecolor("red","blue","green","yellow",46)
    v = input("Choose a another color ")
    if v == "red":
        q = 1
    if v == "green":
        q = 2
    if v == "blue":
        q = 3
    if v == "yellow":
        q = 4
    if v == "random":
        q = randrange(1,4)
    t = t+1
    find(q)
    

def nextcolor2():
    backward(2.5,2)
    changecolor("yellow","red","blue","green",47)
    v = input("Choose a another color ")
    if v == "red":
        q = 1
    if v == "green":
        q = 2
    if v == "blue":
        q = 3
    if v == "yellow":
        q = 4
    if v == "random":
        q = randrange(1,4)
    find(q)

def nextcolor3():
    backward(2.5,2)
    changecolor("green","yellow","red","blue",48)
    v = input("Choose a another color ")
    if v == "red":
        q = 1
    if v == "green":
        q = 2
    if v == "blue":
        q = 3
    if v == "yellow":
        q = 4
    if v == "random":
        q = randrange(1,4)
    find(q)

def nextcolor4():
    backward(2.5,2)
    changecolor("blue","green","yellow","red",49)
    v = input("Choose a another color ")
    if v == "red":
        q = 1
    if v == "green":
        q = 2
    if v == "blue":
        q = 3
    if v == "yellow":
        q = 4
    if v == "random":
        q = randrange(1,4)
    find(q)

def see(q):
    takePicture()
    pic=takePicture()
    x=findColorSpot(pic,q)
    print(x)
    if 132<x<256:
        turnBy(-3)
        see(q)
    if 0<x<125:
        turnBy(3)
        see(q)
    if 124<x<133:
        forward(2.5,2)
        see(q)
    if x == 0:
        turnBy(randrange(25,50))
        see(q)
    if x == -1:
        stop()
        print("Blob Found!")
        if t == 2:
            nextcolor2()
            t == 3
        if t == 1:
            nextcolor1()
            
        if t == 3:
            nextcolor3()
            t == 4
        if t == 4:
            nextcolor4()
            t == 1

def find(q):
    turnBy(randrange(0,45))
    takePicture()
    pic=takePicture()
    x=findColorSpot(pic,q)
    print(x)
    if x>0:
        see(q)
    if x == 0:
        find(q)


t = 1         

print("Choose color: red, blue, green, yellow, or random")
            
c = input("Choose a color ")
print(c)
if c == "red":
    q = 1
if c == "green":
    q = 2
if c == "blue":
    q = 3
if c == "yellow":
    q = 4
if c == "random":
    q = randrange(1,4)
find(q)




