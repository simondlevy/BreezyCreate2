import create2api
import json   # We'll use this to format the output

bot = create2api.Create2()

bot.start()
bot.safe()

print '==============Start Up Data=============='
print json.dumps(bot.sensor_state, indent=4)

print '========================================='
print ''

#Packet 100 contains all sensor data.
bot.get_packet(100)

print '==============Updated Sensors=============='
print json.dumps(bot.sensor_state, indent=4, sort_keys=False)