from speedtest import SpeedTest


speed_test = SpeedTest()

speed_test.start()
new_list = list(range(1, 1000000))
prod = None
for each in new_list:
    each += each
speed_test.finish()

speed_test.start('second')
new_list = list(range(1, 100000000))
prod = None
for each in new_list:
    each += each
speed_test.finish('second')

speed_test.results('second')
