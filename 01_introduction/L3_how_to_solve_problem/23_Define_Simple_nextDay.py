###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    #docstring area
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # my code work but compliexity
    '''
    nextday = day + 1
    dcarry = nextday//31
    if dcarry > 0:
        newday = nextday%31
        if newday == 0:
            newday +=1
    else:
        newday = nextday


    newmonth = month + dcarry

    mcarry = newmonth//13
    if mcarry > 0:
        newmonth = newmonth%13
        if newmonth == 0:
            newmonth +=1

    newyear =year + mcarry

    return newyear,newmonth,newday
    '''

    #keep simple and mechanical
    if day < 30:
        return year,month,day + 1
    else:
        if month < 12:
            return year, month+1,1
        else:
            return year+1, 1,1







#print(nextDay(1999, 12, 30))
#print(nextDay(2013, 1, 30))
#print(nextDay(2012, 12, 30))
#print(nextDay(2012, 12, 1))

print(nextDay(1999, 12, 30 ))
