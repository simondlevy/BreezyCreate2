#!/usr/bin/env python3

'''
roboclient.py

Uses a joystick or other controller to send <X,Y,A> tuples to the create2server
over a socket.

X,Y are control axes (-1..+1); A is autopilot flag (0 or 1).

The MIT License

Copyright (c) 2016 Simon D. Levy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import socket
import pygame

# These should agree with the values in the server script!
#host = '192.168.2.2'
#host = '137.113.118.162'
host = '192.168.2.2'
port = 20000

# Index of base axis of controller
AXIS1 = 0
AXIS2 = 1

# Index of autopilot button
AUTOPILOT_BUTTON = 0

# Connect to the server over a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port)) # Note tuple!

except socket.error as error:
    print('connect() to ' + host + ':' + str(port) + ' failed: ' + str(error))

print('Connected to ' + host + ':' + str(port))

# Set up the joystick
pygame.joystick.init()
pygame.display.init()
try:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    controller.get_axis(AXIS1)
except:
     print('Unable to find joystick / controller')
     exit(1)

# Start with autopilot off
autopilot = False

while True:

    # Force joystick polling
    pygame.event.pump()    
    
    # Pressing autopilot button turns on autopilot; other buttons turn it off
    for k in range(controller.get_numbuttons()):
        if controller.get_button(k):
            if k == AUTOPILOT_BUTTON:
                autopilot = True
            else:
                autopilot = False
    
    # Grab joystick axis values (forward comes in negative)
    axis_x =   controller.get_axis(AXIS1)
    axis_y =  -controller.get_axis(AXIS2)
    
    # Create a fixed-length text message to send to the server
    msg = '%+2.2f %+2.2f %d*' % (axis_x, axis_y, autopilot)

    # Send the message over the socket
    sock.send(msg.encode())

