## Ben Alpert
## BJA282
## September 19, 2017
## Show Bus Locations

from __future__ import print_function
import json
import urllib2 
import os
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python  show_bus_locations_bja282.py YourKeyHere BusLine")
    sys.exit()
    
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

#url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&mode=%s&units=%s&cnt=7&APPID=%s"%(city, mode, units, apikey)
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTA_KEY, BUS_LINE)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

#use the json.loads method to obtain a dictionary representation of the responose string 
mtabuses = json.loads(data)
bus_activity=(mtabuses['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'])
busesontheroad=len(bus_activity[0]['VehicleActivity'])



#Answer Format:
#Bus Line : B52
#Number of Active Buses : 5
#Bus 0 is at latitude 40.687241 and longitude -73.941661
#Bus 1 is at latitude 40.690822 and longitude -73.920759
#Bus 2 is at latitude 40.688363 and longitude -73.979563

print ('Bus Line: %s '%BUS_LINE)
print ('Number of active buses: %s'%(busesontheroad))
for x in range(busesontheroad): 
	print("Bus ", str(x), \
		"is at latitude",bus_activity[0]['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],\
		"and longitude", bus_activity[0]['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
