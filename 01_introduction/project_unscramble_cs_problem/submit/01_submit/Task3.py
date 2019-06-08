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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)
"""
"""
Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.

 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

"""
#################
# handle call only
#################
ans = []
#hasmap={}
incomAns080 = 0
incom080 = 0
totalcallrecords = len(calls)
for idx in range(totalcallrecords):
    incoming = calls[idx][0]
    answering = calls[idx][1]
    #fix line
    if incoming[0]=='(':
        #from Bangalore
        if incoming[1:5] == '080)':
            incom080 +=1
            #print('incoming:',incoming)
            #print('answering:',answering)
            newitem = -1

            # for answering num
            # ans is fix line, save area code
            if '(' == answering[0]:
                right = answering.find(')')
                #print('area code',answering[1:right])
                newitem = answering[1:right]
                # also in Bangalore
                if newitem =='080':
                    incomAns080 +=1
            #ans is mobile, get prfixs
            elif ' ' in answering:
                #print('moblie prefix',answering.split(' ')[0])
                newitem = answering.split(' ')[0][0:4]

            if newitem != -1 and newitem not in ans:
                ans.append(newitem)

#print(ans)
ans = sorted(ans)#in lexicographic order
#print(ans)

print("The numbers called by people in Bangalore have codes:")
for item in range(len(ans)):
    print(ans[item])


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


print("%.2f percent of calls from fixed lines in \
Bangalore are calls to other fixed lines in Bangalore."%(incomAns080 /incom080))
