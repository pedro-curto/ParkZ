# print a different string each time a new image in the images folder is received
# each image comes approximately every 10 seconds but the time may vary
import os
import time

items = previousItems = len(os.listdir('images'))

while True:
    items = len(os.listdir('images'))
    if items != previousItems:
        print('New image received: ' + str(items) + ' images in total')
        previousItems = items
    time.sleep(1)


