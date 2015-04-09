from datetime import datetime

from elasticsearch import helpers
from elasticsearch import Elasticsearch

import xml.etree.ElementTree as ET

import re

es = Elasticsearch()

writeBatchSize = 500

justPrintN = False
n = 1

fromIndex = 'cabi3'
toIndex = 'cabi5'

theType = 'trips'
scrollDur = '30m'

query={"query" : {"match_all" : {}}}
# query = {
#   "query": {
#     "filtered" : {
#       "filter": {
#         "range": {
#           "startDate": {
#               "gte":  "2013-07-01T00:00:00 -0400",
#               "lt":   "2013-07-31T00:00:00 -0400"
#           }
#         }
#       }
#
#     }
#   }
# }

stations = {}

## Stations data
tree = ET.parse('CapitalbikeshareData/bikeStations.xml')
root = tree.getroot()
for child in root:
    station = {}
    for grandchild in child:
        station[grandchild.tag] = grandchild.text
    stations[ station[u'name'] ] = station


## mutate function
def mutateDocument( source ):
    try:
        startStation = stations[source['startStation']]
        source['startLocation'] = [ float(startStation[u'long']), float(startStation[u'lat']) ]
    except KeyError:
        ##print "no start station: " + source['startStation']
        ##source['startLocation'] = [-77.1412335, 38.9621287 ]
        source['todo'] = 'noLocation'
    try:
        endStation = stations[source['endStation']]
        source['endLocation'] = [ float(endStation[u'long']), float(endStation[u'lat']) ]
    except KeyError:
        ##print "no end station: " + source['endStation']
        ##source['endLocation'] = [-77.1412335, 38.9621287 ]
        source['todo'] = 'noLocation'
    ## Already Processed
    # # correct subType
    # origSubType = source['subType'].lower()
    # newSubType = 'subscriber' if origSubType == 'registered' else origSubType
    # source['subType'] = newSubType
    #
    # # correctUnits of Duration
    # source['duration'] = round(float(source['duration']) / 60.0 , 2) #convert to minutes
    #
    # source['endStation'] = re.sub('\s\([0-9]*\)$', '',  source['endStation'] )
    # source['startStation'] = re.sub('\s\([0-9]*\)$', '',  source['startStation'] )
    # source['behavior'] = 'roundTrip' if source['endStation'] == source['startStation'] else 'pointToPoint'
    return source



# loop over all all documents with a scroll
bulkActions = []
counter = 0
for doc in helpers.scan( client=es, index=fromIndex, doc_type=theType, query=query, scroll=scrollDur ):
    counter = counter + 1
    theId = doc['_id']
    source = doc['_source']
    
    ## perform mutations
    alteredSource = mutateDocument( source )
    
    ## create and queue action
    action = {
        "_index": toIndex,
        "_type": theType,
        "_id": theId,
        "_source": alteredSource
    }
    bulkActions.append( action )
    if(justPrintN):
        print alteredSource
    
    ## every writeBatchSize actions are written to the new index
    if(len(bulkActions) >= writeBatchSize ):
        if(not justPrintN):
            helpers.bulk( es,  bulkActions )
        bulkActions = []
    ## print some status
    if(counter % 10000 == 0):
        print "Copying from " + fromIndex + " to " + toIndex + ": " + str(counter)
    if(justPrintN and counter == n):
        raise SystemExit


if(len(bulkActions) > 0):
    if(not justPrintN):
        helpers.bulk( es,  bulkActions )
    bulkActions = []


