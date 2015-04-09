# Import Libraries
from elasticsearch import Elasticsearch
from elasticsearch import helpers

import json
from datetime import datetime

outputFileNameWithoutExtension = 'extract'
outputFileNameExtension = ".json"
sourceIndex = 'cabi5'
sourceType = 'trips'
docsPerFile = 100000
printPerDoc = 10000

fileCounter = 0
currentDocName = ""

def genFileName():
    global currentDocName
    global fileCounter
    fileCounter = fileCounter + 1
    fileName = outputFileNameWithoutExtension + "-" + str(fileCounter) + outputFileNameExtension
    currentDocName = str(fileName)
    return fileName

f = open(genFileName(), 'w')
print "Closing ", currentDocName
docInFileCounter = 0
def pushDocToFile( doc ): 
    global f       
    global docInFileCounter
    meta = {"index": {"_id": doc[u'_id']}}
    source = doc[u'_source']
    
    f.write(json.dumps(meta) + "\n")
    f.write(json.dumps(source) + "\n")
        
    if(docInFileCounter >= docsPerFile - 1):
        f.close()
        print "Closing ", currentDocName 
        docInFileCounter = 0
        f = open(genFileName(), 'w')
        print "Opening ", currentDocName
    else:
        docInFileCounter = docInFileCounter + 1


print "Starting extact of index ", sourceIndex, " with type ", sourceType
counter = 0
es = Elasticsearch()
for doc in helpers.scan( es, query=None, scroll='10m', index=sourceIndex, doc_type=sourceType ):
    if(counter % printPerDoc == 0):
        print "  Export on doc: ", counter
    counter = counter + 1
    pushDocToFile(doc)


##close last file handle when done
f.close()
print "Closing ", currentDocName 