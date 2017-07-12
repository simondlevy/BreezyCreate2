#!/usr/bin/env python3

'''
robosong.py - Use BreezyCreate2 to play a familiar melody

This code is part of BreezyCreate2

The MIT License

Copyright (c) 2017 Virginia Summer STEAM team + Simon D. Levy

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

from breezycreate2 import Robot
import time

# Triples: (note,duration,pause)
MELODY = [('C4',10,0.2),
         ('C4',13,0.26),
         ('C4',15,0.3),
         ('F4',45,0.9),
         ('C4',45,0.9),
         ('F4',10,0.2),
         ('C4',13,0.26),
         ('F4',15,0.3),
         ('A4',45,0.9),
         ('F4',45,0.9),
         ('A4',10,0.2),
         ('F4',13,0.26),
         ('A4',15,0.3),
         ('C5',45,0.9),
         ('C4',45,0.9),
         ('A4',10,0.2),
         ('F4',13,0.26),
         ('A4',15,0.3),
         ('C5',45,2.2)]

'''
# Another popular melody
MELODY   = [('C4',11,0.3),
            ('C4',11,0.3),
            ('C4',11,0.3),
            ('C4',32,0.7),
            ('G4',32,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('D4',11,0.3),
            ('C5',64,1.2),
            ('G4',40,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('D4',11,0.3),
            ('C5',64,1.2),
            ('G4',40,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('F4',11,0.3),
            ('D4',64,2) ]
'''

# Create a Create2. This will automatically try to connect to your robot over serial
bot = Robot()

# Play the melody
for triple in MELODY:
    bot.playNote(triple[0], triple[1])
    time.sleep(triple[2])

# Close the connection
bot.close()
