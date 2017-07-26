""" Query archiver repeatedly for speed test

"""

import urllib.request
import timeit

'''
z = urllib.request.urlopen("https://pswww.slac.stanford.edu/epics/retrieval/data/getData.json?pv=GDET%3AFEE1%3A241%3AENRC",timeout=10);

for i in range(10):
    print(z.readline())


u = urllib.request.urlopen("https://pswww.slac.stanford.edu/epics/retrieval/data/getData.json?pv=GDET%3AFEE1%3A241%3AENRC&from=2017-06-06T01%3A01%3A00.000Z&to=2017-06-06T01%3A01%3A10.000Z",timeout=10);

for i in range(10):
    print(u.readline())

'''

def test():
    u=urllib.request.urlopen("https://pswww.slac.stanford.edu/epics/retrieval/data/getData.json?pv=GDET%3AFEE1%3A241%3AENRC&from=2017-06-06T01%3A01%3A00.000Z&to=2017-06-06T02%3A01%3A10.000Z",timeout=10)
    return 0



#for i in range(100):
#    print(u.readline())


n = 100
res = timeit.timeit(test,number=n)
print("n:  \t",n)
print("res:\t",res)
print("avg:\t",res/n)


