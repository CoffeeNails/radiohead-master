import time
import sys
import urllib3
from time import sleep
import json
import csv
import datetime
import requests
from datetime import datetime
import subprocess # just for changing file ownership at the end of script
http = urllib3.PoolManager()

###############################################################################
DURATION = 2000 # How many timestamps you want? it 100 takes 10s
TIMES = 10 # How many times per sec you want the timestamp
###############################################################################

### define filename to save timestamps (coords3.csv)
with open('coords.csv', mode='w') as csvfile: # open the csv file

    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["X", "Y", "orientation","timestamp"])
    print ("Coord queries running, wait"),
    print(DURATION/TIMES),
    print ("s")

    def main():

        #######################################################################
        ### change the url localhost to match actual addrest for REST API calls
        #######################################################################
        url = 'http://192.168.12.20/api/v2.0.0/status' # url where to call the rest api
        error=0
        response = http.request('GET', url) # response values from REST API

        ### get the values from response jason object x,y,orientation ###
        try:
            x = json.loads(response.data)['position']['x']
            y = json.loads(response.data)['position']['y']
            orientation = json.loads(response.data)['position']['orientation']
        except KeyError as error:
            error=1

        ###  get the timestamp %f')[:-3] gives second with 3 digits ###
        timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3]

        ### write the REST API values into csv file
        if error != 1:
            writer.writerow([x,y,orientation,timestamp])
        else: 
            error=0

    if __name__ == '__main__':
        time_start = time.time()

        i = 1
        while True:
            time_current = time.time()
            if time_current > time_start + i / float(TIMES):
                # print('{}: {}'.format(i, time_current))
                main() # execute main function after every 100ms
                i += 1
            if i > DURATION: # break the prog when duration reached
                break

print ("Coord queries done, have a nice day!")
################################################################################
### If issues with ownership of the file u can use subprocess.call function to
### execute shell commands such as:
### subprocess.call(['chown', '[user]:root','/home/user/Documents/coords3.csv'])
### change [user] to match username and the file path to correct folder
################################################################################
