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
cars2 = [{
             "id":"1",
             "driver":"Todd Kelly",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-TK-JDR---side-view1.jpg"},
         {
            "id":"2",
             "driver":"Chas Mostert",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-CM-FPR---side-view1.jpg"},
         {
             "id":"3",
             "driver":"Mark Winterbottom",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-MW-FPR---side-view1.jpg"},
         {
             "id":"4",
             "driver":"Craig Lowndes",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-CL-Red-Bull---side-view1.jpg"},
         {
             "id":"5",
             "driver":"Garth Tander",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-GT-HRT---side-view.jpg"},
         {
             "id":"6",
             "driver":"Russell Ingall",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-LDM---side-view.jpg"},
         {
             "id":"7",
             "driver":"Tim Slade",
             "image":"http://d508o84lonf06.cloudfront.net/live/images/car/profileList/2014-SCAR---side-view.jpg"}
    ]
lap = 1
racetime = time.time()
# 3.3 mins for a lap
laptime_max = 60 * 3.3
lapvariance = 30
while True:

    if lap > 30:
        lap = 0
    current_time = int(racetime + (laptime_max * lap))
    max_lap = current_time + int(laptime_max)
    for car in cars2:
        laptime = random.randrange(current_time,max_lap,lapvariance)
        speed = {
            "speed":random.randrange(100,200,10),
            "laptime":time.strftime("%H:%M:%S",time.localtime(racetime-laptime)),
            "laptime_unix":laptime,
            "lap":lap,
            "driver":car["driver"],
            "image":car["image"]

        }
        r = requests.put(fbapp + base + car["id"] + "/data.json", data=json.dumps(speed))
        print r.text
    lap += 1
