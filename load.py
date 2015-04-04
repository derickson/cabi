# Import Libraries
from datetime import datetime
import pyelasticsearch

es = pyelasticsearch.ElasticSearch('http://localhost:9200/')

import fileinput

## set to true to test parsing only
debugTrip = False

def indexBulk(bulkObjs):
    if(not debugTrip):
        es.bulk((es.index_op(doc) for doc in bulkObjs), index='cabi', doc_type='trips')


def checkDateFormat( dateStr, format ):
    try:
        datetime.strptime( dateStr, format )
        return True
    except ValueError:
        return False


def convertToISO8601( dateStr ):
    format1 = "%m/%d/%Y %H:%M"
    format2 = "%Y-%m-%d %H:%M"
    
    if(checkDateFormat(dateStr, format1)):
        return datetime.strptime(dateStr, format1).isoformat()
    if(checkDateFormat(dateStr, format2)):
        return datetime.strptime(dateStr, format2).isoformat()
    raise Exception( 'dateString was not of known format: ' + dateStr)


def constructObj( line, index ):
    parts = line.split(',')
    if(debugTrip):
        print index, str(parts)
    timeparts = parts[0].translate( None, ''.join([ 'min.', 'sec.', 'h','m','s'])).split(' ')
    duration = int(timeparts[0]) * 3600 + int(timeparts[1]) * 60 + int(timeparts[2])
    obj =  { 
        'duration': duration,
        'startDate': convertToISO8601(parts[1]) + ' -0400',
        'endDate': convertToISO8601(parts[2]) + ' -0400',
        'startStation': parts[3],
        'endStation': parts[4],
        'bikeNum': parts[5],
        'subType': parts[6]
    }
    if(debugTrip):
        print obj
    return obj
    


counter = 0
bulkCounter = 0
bulkObjs = []
for line in fileinput.input():
    if counter > 0:
        bulkObjs.append( constructObj(line.strip(), counter) )
        bulkCounter = bulkCounter + 1
        if(bulkCounter >= 500):
            indexBulk(bulkObjs)
            bulkObjs = []
            bulkCounter = 0
    if debugTrip and counter > 5:
        break
    counter = counter + 1
    if counter % 1000 == 0:
        print "On line: ", counter
if(bulkCounter > 0):
    indexBulk(bulkObjs)
    bulkCounter = 0