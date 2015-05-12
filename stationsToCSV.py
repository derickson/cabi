from datetime import datetime

import xml.etree.ElementTree as ET

import re


## Stations data
tree = ET.parse('CapitalbikeshareData/bikeStations.xml')
root = tree.getroot()
for child in root:
    station = {}
    for grandchild in child:
        station[grandchild.tag] = grandchild.text
    print station[u'name'] +","+ station[u'lat'] +","+ station[u'long']