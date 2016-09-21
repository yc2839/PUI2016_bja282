## Ben Alpert
## BJA282
## September 19, 2017
## Get Bus Info

from __future__ import print_function
import json
import urllib2 
import os
import sys
import pandas as pd

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python get_bus_info_bja282.py APIKey BusLine file_to_write_to.csv")
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
#Latitude,Longitude,Stop Name,Stop Status
#40.755489,-73.987347,7 AV/W 41 ST,at stop
#40.775657,-73.982036,BROADWAY/W 69 ST,approaching
#40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
#40.764998,-73.980416,N/A,N/A
#40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
#40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
#40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away

columns = ['Latitude','Longitude','Stop Name','Stop Status']
tableframe = pd.DataFrame(columns=columns)


print ('Bus Line: %s '%BUS_LINE)
print ('Number of active buses: %s'%(busesontheroad))

for y in range(busesontheroad):
  tableframe.loc[y, 'Latitude']=bus_activity[0]['VehicleActivity'][y]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
  tableframe.loc[y, 'Longitude']=bus_activity[0]['VehicleActivity'][y]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

  stop_name = (bus_activity[0]['VehicleActivity'][y]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])

  if ('stop_name'=={}):
    tableframe.loc[y, 'Stop Name']="N/A"
    tableframe.loc[y, 'Stop Status']="N/A"
  else:
    tableframe.loc[y, 'Stop Name']=bus_activity[0]['VehicleActivity'][y]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    tableframe.loc[y, 'Stop Status']=bus_activity[0]['VehicleActivity'][y]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']\
    ['Distances']['PresentableDistance']

print (tableframe)
tableframe.to_csv(sys.argv[3], index=False)
