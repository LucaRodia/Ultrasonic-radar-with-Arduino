# goal
# take data from the arduino -> plot a cv2 radar image

import serial
import time
import cv2 as cv
import numpy as np
import math

arduinoData = serial.Serial("/dev/ttyACM0", 9600, timeout=2)
time.sleep(5)


width = 1280
height = 720
img = np.zeros([height, width, 3], dtype=np.uint8)


distanceDict = dict()  #key -> angle, object -> [distance, intensity] --- the intensity will decrease over time

def deg2Rad(angle):
    return angle*2*math.pi/360

def updateDict(Dict):
    for el in Dict:
        dist, intensity = Dict[el]
        intensity -= 30
        Dict[el] = [dist, intensity]

def y(y0, m, dx):
    y = y0 - abs(m*dx)
    return y

def printImage(img, l, h, dict):    # l, h are the image width and height
    k = 20  # needed for the drawing starting point
    max_dist = 500    #it's the maximum distance from the center
    for angle in dict:
        distance, intensity = dict[angle]
        m = math.tan(deg2Rad(angle))
        deltaX = k*distance/math.sqrt(m**2 +1)
        
        if angle < 90:
            x_i, x_f = math.floor(l/2 - deltaX), math.floor(l/2 - max_dist)
            y_i, y_f = math.floor(y(h, m, deltaX)), math.floor(y(h, m, max_dist))
        elif angle > 90:
            x_i, x_f = math.floor(l/2 + deltaX), math.floor(l/2 + max_dist)
            y_i, y_f = math.floor(y(h, m, deltaX)), math.floor(y(h, m, max_dist))           
        else:
            x_i, x_f = l/2, l/2
            y_i, y_f = k*distance, h - max_dist

        cv.line(img, (x_i, y_i), (x_f, y_f), (0, intensity, 0), thickness=3)
    cv.imshow("radar", img)
    cv.waitKey(10)  #it waits 40 ms before destroyng the window



while True:
    data = arduinoData.readline().decode().strip()
    if data:
        print(data)
        try:
            splitted = data.split("/")
            distance, angle = int(splitted[0]), int(splitted[1])
            #distance, angle = int(distance), int(angle)
            #print(splitted)
            print("Distanza: ", distance, " Angolo: ", angle) 
            distanceDict[distance] = [angle, 255]  #255 is the maximum intensity
            updateDict(distanceDict)
            printImage(img, width, height, distanceDict)
            time.sleep(0.02)
        except IndexError:
            print("un solo valore")
        except ValueError:
            print("Errore, non ho un numero intero!!")
        except UnicodeDecodeError:
            print("Unicode error")






