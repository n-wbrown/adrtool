import urllib.request
import datetime

class ArchiverQuery:

    def __init__( self,
                  base="https://pswww.slac.stanford.edu/epics/retrieval/data/getData",):
        self.base=base
    
    def get(self,start,end,pv,dtype):

        url_components = {
            'base':self.base,
            'start':start.isoformat().replace(":","%3A")+".000Z",
            'end':end.isoformat().replace(":","%3A")+".000Z",
            'dtype':"."+dtype,
            'pv':pv.replace(":","%3A"),
        }
        query_string_base = "{base}{dtype}?pv={pv}&from={start}&to={end}".format(**url_components)
        #print(query_string_base)
        #z should be a filelike object containging formatted data
        z=urllib.request.urlopen(query_string_base,timeout=5)
        for f in z:
            print(f)
        '''
        for i in range(10):
            print(z.readline())
        '''


#example usage, uncomment to run:
"""
u = ArchiverQuery()
l = u.get(datetime.datetime(2017,6,6,0,9,0),datetime.datetime(2017,6,6,0,10,0),"GDET:FEE1:241:ENRC","json")
print(l)
"""

#example/target URL
"""
https://pswww.slac.stanford.edu/epics/retrieval/data/getData.json?pv=GDET%3AFEE1%3A241%3AENRC&from=2017-06-06T01%3A01%3A00.000Z&to=2017-06-06T01%3A01%3A10.000Z

"""
