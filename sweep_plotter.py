#grafico
import cv2 as cv 
import numpy as np
import math


imgWidth = 1280
imgHeight = 720
img = np.zeros((imgHeight, imgWidth, 3), dtype=np.uint8)

k = 5   #it's a constant. Proportional to the distance. Used for the start of the line
max_dist = 500  #it's the distance limit from the center of the image -> te effective point has to change depending on the angle
test_distance = 20


angles = []
for i in range(60):
    angles.append(i*3)
print(angles)

def degres2Rad(angle):
    return angle*2*math.pi/360

def getX(angle, k, dist, max_dist, imgWidth):
    if angle < 90:
        xi, xf = imgWidth/2 - k*dist/math.sqrt(math.tan(degres2Rad(angle))**2 + 1), imgWidth/2 - max_dist
    elif angle > 90:
        xi, xf = imgWidth/2 + k*dist/math.sqrt(math.tan(degres2Rad(angle))**2 + 1), imgWidth/2 + max_dist
    elif angle == 90:
        xi, xf = 0, 0

    return math.floor(xi), math.floor(xf)

def segEquation(x, angle, imgWidth, imgHeight, dist): #given an x it returns the y point
    if angle != 90:
        m = math.tan(degres2Rad(angle))
        print(m)
        y = imgHeight - abs(m*(x-imgWidth/2))
    else:
        y = dist*5
    return math.floor(y)

def main():

    for angle in angles:
        x_in, x_fin = getX(angle, k, test_distance, max_dist, imgWidth)
        print(angle, x_in, segEquation(x_in, angle, imgWidth, imgHeight, test_distance))
        cv.line(img, (x_in, segEquation(x_in, angle, imgWidth, imgHeight, test_distance)), (x_fin, segEquation(x_fin, angle, imgWidth, imgHeight, test_distance)), color=(255, 0, 0), thickness=3)
        cv.imshow("prova", img)
        cv.waitKey(0)


main()