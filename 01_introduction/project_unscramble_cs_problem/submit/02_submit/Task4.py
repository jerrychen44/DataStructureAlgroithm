"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:

these are numbers that
1. make outgoing calls
        but never
            a.send texts,
            b.receive texts
            c.receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



outgoingcallset = set([record[0] for record in calls])
receivingcallset = set([record[1] for record in calls])
outgoingtextset = set([record[0] for record in texts])
receivingtextset = set([record[1] for record in texts])

outgoincalllist = list (outgoingcallset)
################
# checking the ruls
# make outgoing calls
#        but never
#            a.send texts,
#            b.receive texts
#            c.receive incoming calls.
################
ans = []
for num in outgoincalllist:
    if num not in outgoingtextset and num not in receivingtextset and num not in receivingcallset:
        ans.append(num)


#in lexicographic order
ans = sorted(ans)


print('These numbers could be telemarketers:')
for num in ans:
    print(num)
