__author__ = 'andrew sinclair'

'''
Very simple example that sends some random values to firebase to simulate car speeds
The aim is a demo of using firebase for real time stats
'''

import random
import requests
import json
import time

fbapp = "https://sportstest2.firebaseio.com/"

base = "car/"

cars = ['red','blue','green','black','orange','yellow','brown','pink']
lap = 1
racetime = time.time()
# 3.3 mins for a lap
laptime_max = 60 * 3.3
lapvariance = 30
while True:
    lap += 1
    if lap > 30:
        lap = 0
    current_time = int(racetime + (laptime_max * lap))
    max_lap = current_time + int(laptime_max)
    for car in cars:
        laptime = random.randrange(current_time,max_lap,lapvariance)
        speed = {
            "speed":random.randrange(100,200,10),
            "laptime":time.strftime("%H:%M:%S",time.localtime(laptime)),
            "laptime_unix":laptime,
            "lap":lap
        }
        r = requests.put(fbapp + base + car + "/data.json", data=json.dumps(speed))
        print r.text
