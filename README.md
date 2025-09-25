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
This script reads the angle θ from the serial port and calculates the equation of a straight line forming that angle with the bottom edge of the screen.

Using trigonometric functions (primarily tangent) and linear transformations, it derives the correct line equation to visualize the radar sweep.

The start point of the line is determined by a coefficient k, which scales proportionally to the measured distance (also read from the serial port). This simulates the effect of the detected object’s position in space.

## Known Issues / Future Improvements

#### Unstable serial communication
The data received from the serial port can be unreliable. A potential solution is to delegate data transmission to a dedicated component or microcontroller, improving consistency.

#### Incorrect distance projection
The current method uses a linear proportionality between the distance and the start of the plotted line (x₀). This distorts the circular sweep effect: the arc appears shrinked near the center and stretched near the edges.
To correct this, distance should be projected onto the bottom axis, preserving the circular symmetry and generating a proper radar-like sweep.
