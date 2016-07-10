#!/usr/bin/env python3

from breezycreate2 import Robot
import time

# Create a Create2. This will automatically try to connect to your robot over serial
bot = Robot()

# Play a note to let us know you're alive!
bot.playNote('A4', 100)

# Tell the Create2 to drive straight forward at a speed of 100 mm/s
bot.setTurnSpeed(50)

# Wait a second
time.sleep(1)

# Stop
bot.setTurnSpeed(0)

# Listen for bumper hits for a few seconds
start_time = time.time()
while (time.time() - start_time) < 3:
    
    print(bot.getBumpers())

# Close the connection
bot.close()
