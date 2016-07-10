import create2api
import time

#Create a Create2 Bot

bot = create2api.Create2()

bot.start()
bot.safe()


# time.sleep(10)

# bot.set_day_time('Friday', 17, 40)

print 'Voltage: ' + str(bot.sensors['voltage'])
print 'OI mode: ' + str(bot.sensors['oi mode'])
print 'Battery temperature: ' + str(bot.sensors['temperature'])

# print 'forwad'
# bot.drive_straight(200)
# #bot.drive(-200, 500)

# time.sleep(1)
# print 'back'
# bot.drive_straight(-200)
# #bot.drive(200, 500)
# time.sleep(1)
# print 'Stop Driving'
# #bot.drive(0,0)
# bot.drive_straight(0)
# bot.reset()


bot.destroy()