import os
import csv
import sys
import subprocess

file = open(sys.argv[1], 'r')
reader = csv.reader(file)

# CSV Format name,url,username,password
NAME = 0
URL = 1
USERNAME = 2
PASSWORD = 3

for row in reader:
    # Android app username/password is stored without a name value. We ignore them for this
    if len(row[NAME]) > 0:
        website = None

        # Clean www. from preceding websites because it's weird and ugly
        if row[NAME].startswith("www."):
            website = row[NAME][4:]
        else:
            website = row[NAME]

        # data passed into storage
        payload = row[PASSWORD]+"\nusername: "+row[USERNAME]

        temp = subprocess.run(["pass", "insert", "--multiline", "web/"+website], input=str.encode(payload))

file.close()
