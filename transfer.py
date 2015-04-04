from datetime import datetime

from elasticsearch import helpers
from elasticsearch import Elasticsearch


es = Elasticsearch()






##from pyelasticsearch import ElasticSearch
##es = ElasticSearch('http://localhost:9200/')



##helpers.reindex( es, 'cabi', 'cabi2')

writeBatchSize = 5000


theType = 'trips'
fromIndex = 'cabi2'
toIndex = 'cabi3'

scrollDur = '1m'

query={"query" : {"match_all" : {}}}

bulkActions = []
counter = 0
for doc in helpers.scan( client=es, index=fromIndex, doc_type=theType, query=query, scroll=scrollDur ):
    counter = counter + 1
    theId = doc['_id']
    source = doc['_source']
    
    # correct subType
    origSubType = source['subType'].lower()
    newSubType = 'subscriber' if origSubType == 'registered' else origSubType
    source['subType'] = newSubType

    action = {
        "_index": toIndex,
        "_type": theType,
        "_id": theId,
        "_source": source
    }
    bulkActions.append( action )
    
    if(len(bulkActions) >= writeBatchSize ):
        helpers.bulk( es,  bulkActions )
        bulkActions = []
    if(counter % 10000 == 0):
        print "Copying from " + fromIndex + " to " + toIndex + ": " + str(counter)
    ##if(counter == 5000):
    ##    raise SystemExit


if(len(bulkItems) > 0):
    helpers.bulk( es,  bulkActions )
    bulkItems = []


# scanResp = es.search( index="cabi2", doc_type="trips", body=query, search_type="scan", scroll=scrollDur )
#
# totalToScan = scanResp[u'hits'][u'total']
# scrollId = scanResp[u'_scroll_id']
#
# print totalToScan
# print scrollId
#
#
# response = es.scroll(scroll_id=scrollId, scroll=scrollDur)
# print response


#count = 0

#helpers.scan( es, )


## es.bulk((es.index_op(doc, id=doc.pop('id')) for doc in docs),
##          index='contacts',
##          doc_type='person')