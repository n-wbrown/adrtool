"""Some hand-written test URLs that extract data from the archiver

"""

import urllib.request



z = urllib.request.urlopen("https://pswww.slac.stanford.edu/epics/retrieval/data/getData.json?pv=GDET%3AFEE1%3A241%3AENRC",timeout=10);

for i in range(10):
    print(z.readline())


u = urllib.request.urlopen("https://pswww.slac.stanford.edu/epics/retrieval/data/getData.json?pv=GDET%3AFEE1%3A241%3AENRC&from=2017-06-06T01%3A01%3A00.000Z&to=2017-06-06T01%3A01%3A10.000Z",timeout=10);

for i in range(10):
    print(u.readline())


