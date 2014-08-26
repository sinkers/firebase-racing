__author__ = 'andrew sinclair'

'''
Very simple example that sends some random values to firebase to simulate car speeds
The aim is a demo of using firebase for real time stats
'''

import random
import requests
import json

fbapp = "https://sportstest2.firebaseio.com/"

base = "car/"

cars = ['red','blue','green','black','orange','yellow','brown','pink']

while True:
    for car in cars:
        speed = {"speed":random.randrange(100,200,10)}
        r = requests.put(fbapp + base + car + "/speed.json", data=json.dumps(speed))
        print r.text
