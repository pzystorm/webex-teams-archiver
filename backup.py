#!/usr/bin/python3

from webexteamsarchiver2 import WebexTeamsArchiver
import sys
import requests

if len(sys.argv) != 2 or not sys.argv[1]:
  print("ERROR! 1st parameter must be given: Bearer")
  sys.exit(1)

archiver = WebexTeamsArchiver(sys.argv[1])
headers = {'Authorization': 'Bearer '+sys.argv[1]}
r = requests.get("https://webexapis.com/v1/rooms?max=1000", headers=headers)
total=len(r.json()['items']);
i=0
for room in r.json()['items']:
  i=i+1
  print( "Processing " + str(i) + "/" + str(total) + ": " + str(room) )
  archiver.archive_room(room['id'])
