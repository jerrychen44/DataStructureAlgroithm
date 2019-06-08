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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

'''
All telephone numbers are 10 numerical digits long.
Each telephone number starts with a code indicating the location and/or type of the telephone number.
There are three different kinds of telephone numbers, each with a different format:

1.Fixed lines start with an area code enclosed in brackets.
The area codes vary in length but always begin with 0. Example: (022)40840621.

2.Mobile numbers have no parentheses, but have a space in the middle of the number to help readability.
The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9.
Example: 93412 66159.

3.Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: 1402316533.

'''

def updatehashmap(hashmap,num):

    if num not in hashmap:
        hashmap[num] = 1
    else:
        hashmap[num] +=1





hashmap = {}# number str: count
################################
# handle text csv
################################
totaltextsrecords = len(texts)
#print(totaltextsrecords)

for idx in range(totaltextsrecords):
    incoming = texts[idx][0]
    answering = texts[idx][1]
    updatehashmap(hashmap,incoming)
    updatehashmap(hashmap,answering)


################################
# handle call csv
################################
totalcallrecords = len(calls)

#time O(M)
for idx in range(totalcallrecords):
    incoming = calls[idx][0]
    answering = calls[idx][1]

    updatehashmap(hashmap,incoming)
    updatehashmap(hashmap,answering)



#Time O(N+M), N = texts records, M = call records
#Space O(N+M) for hashmap in worst case
print("There are %d different telephone numbers in the records."%(len(hashmap)))
