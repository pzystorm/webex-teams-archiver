#!/usr/bin/python3

from webexteamsarchiver2.webexteamsarchiver import WebexTeamsArchiver
import sys
import requests

if len(sys.argv) != 2 or not sys.argv[1]:
  print("ERROR! 1st parameter must be given: Bearer")
  sys.exit(1)

archiver = WebexTeamsArchiver(sys.argv[1])
headers = {'Authorization': 'Bearer '+sys.argv[1]}
r = requests.get("https://webexapis.com/v1/rooms?max=1000", headers=headers)
if r.status_code != 200:
  print("ERROR! HTTP Response Code: " + str(r.status_code))
  sys.exit(1)
if "items" not in r.json():
  print("ERROR! No items (channels) in response")
  sys.exit(1)

total=len(r.json()['items']);
i=0
for room in r.json()['items']:
  i=i+1
  print( "Processing " + str(i) + "/" + str(total) + ": " + str(room) )
  archiver.archive_room(room['id'])
