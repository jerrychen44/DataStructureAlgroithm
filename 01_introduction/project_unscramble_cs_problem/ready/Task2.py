"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import operator
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def updatehashmapMax(hashmap,num,duraing):

    if num not in hashmap:
        hashmap[num] = duraing
    else:
        hashmap[num] +=duraing

    #tracking max
    global maxduraing
    global maxnumb

    if hashmap[num] > maxduraing:
        maxduraing = hashmap[num]
        maxnumb = num



###############
# for call csv only
###############
hashmap = {}
totalcallrecords = len(calls)
maxduraing = -1
maxnumb = ''

for idx in range(totalcallrecords):
    incoming = calls[idx][0]
    answering = calls[idx][1]
    duraing = int(calls[idx][3])

    updatehashmapMax(hashmap,incoming,duraing)
    updatehashmapMax(hashmap,answering,duraing)


print("%s spent the longest time, %d seconds, on the phone during September 2016."%(maxnumb,maxduraing))
