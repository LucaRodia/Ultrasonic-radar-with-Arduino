# Ultrasonic-radar-with-Arduino
The project aims to build a radar using only an ultrasonic distance sensor and a servo motor connected to an Arduino board.

## Brief code explaination

#### servo_control.ino
This script controls the sensor and the actuator.
It keeps the servo rotating between 0° and 180° by changing the goal of the servo every iteration (using a proper delay) adding a dx angle to the current goal.
When 0° or 180° are reached, dx gets his sign changed (dx = -dx).

The ultrasonic distance sensor gets the distance (converting the travel time of the sound into cm) and writes it on the serial port.

#### data_reception_tester.py
Simpe script to check is the serial communication between Arduino and VSCode is working.

#### sweep_plotter.py
Given the angle theta (from serial port) it calculates the proper equation to plot a straight line with and angle theta in respect to the bottom of the screen.
It uses tangent and linear translations to get the equation of the line.

Then based on a coefficient k (arbitrary) it sets the beginning of the plotted line proportionally to the distance (from serial port).


## Problems/Future improovements

1. The serial port looks instable --> find a better way to transmit data. Current idea: use another component just to transmit datas.
2. Improove x0 (the beginning of the plotted line). Currently x0 distance from the origin is proportional to the distance, but to get a circle we need to consider the projection on the bottom, otherwise the circunference gets shrinked in the middle and stretche on the borders.
