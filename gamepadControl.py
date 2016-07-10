import create2api
import xbox_read
# Xbox_read can be found at https://github.com/zephod/lego-pi/blob/master/lib/xbox_read.py

bot = create2api.Create2()

print '==============Starting up Create 2=============='
bot.start()
bot.safe()

thumbstickMin = -32768
thumbstickMax = 32767

def mapValue(value, leftMin, leftMax, rightMin, rightMax):
    # Taken from http://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

for event in xbox_read.event_stream(deadzone=12000):
    #Left thumbstick up/down controls speed
    if event.key == 'Y1':
        #map the thumbstick's value to the bot's driving speed
        vel = mapValue(event.value, thumbstickMin, thumbstickMax, -250, 250)
        print 'Driving'
        bot.drive_straight(vel)
    
    #Right thumbstick left/right controls rotation
    if event.key == 'X2':
        # Map the thumbstick's value to the bot's rotation
        if event.value > 0:
            # Thumbstick moved right
            print 'Steering Right'
            print event.value
            vel = mapValue(event.value, 0, thumbstickMax, 0, 100)
            bot.turn_clockwise(vel)
        if event.value < 0 :
            # Thumbstick moved left
            print 'Steering Left'
            print event.value
            vel = mapValue(event.value, thumbstickMin, 0, -100, 0)
            bot.turn_counter_clockwise(vel)
        
