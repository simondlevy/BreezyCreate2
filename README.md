# Create2API
A python library for controlling the iRobot Create 2

###Simple
Create2API is made to give simple access to basic, often used functions on the iRobot Create 2. It keeps all the important info about your Create 2 in an easy to access JSON file.

###Safe
Create2API has a lot of checks in place to make sure you don't send a bad command to your robot. If something won't work, Create2API will let you know!

###Easy to use
Create2API is meant to be interacted with through a single class: "Create2". Interacting with your bot is a breeze:

```python
import create2api
import time

#Create a Create2. This will automatically try to connect to your
#	robot over serial
bot = create2api.Create2()

#Start the Create2
bot.start()

#Put the Create2 into 'safe' mode so we can drive it
bot.safe()

#Tell the Create2 to drive straight forward at a speed of 100 mm/s
bot.drive_straight(100)

#Wait for 5 seconds
time.sleep(5)

#Tell the Create2 to drive straight backward at a speed of 100 mm/s
bot.drive_straight(-100)

#Wait for 5 seconds
time.sleep(5)

#Stop the bot
bot.drive_straight(0)

#Close the connection
bot.destroy()

```


##Implemented OI codes
- Start
- Reset
- Stop
- Baud
- Safe
- Full
- Clean
- Max
- Spot
- Seek Dock
- Power (Off)
- Set Day/Time
- Drive
- Motors PWM
- Digit LED ASCII
- Sensors

##Unimplemented OI codes
- Schedule
- Drive Direct
- Drive PWM
- Motors
- LED
- Scheduling LED
- Digit LED Raw
- Buttons
- Song
- Play
- Query List
- Stream
- Pause/Resume Stream