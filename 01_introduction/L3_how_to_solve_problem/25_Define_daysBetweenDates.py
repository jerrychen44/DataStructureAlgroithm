# -*- coding: utf-8 -*-

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def isLeapYear(year):
    '''
    if year % 4 !=0:
        return False #common year
    elif year % 100 !=0:
        return True
    elif year % 400 !=0:
        return False #common year
    else:
        return True
    '''

    if year % 4 !=0:
        return False #common year
    elif year % 100 !=0:
        return True
    elif year % 400 !=0:
        return False #common year
    else:
        return True



def daysinMonth(year,month):
    '''
                    Chronology	Alphabetic	Days
                    1	January	31 days
                    2	February	28 days, 29 in leap years
                    3	March	31 days
                    4	April	30 days
                    5	May	31 days
                    6	June	30 days
                    7	July	31 days
                    8	August	31 days
                    9	September	30 days
                    10	October	31 days
                    11	November	30 days
                    12	December	31 days

    '''
    if month ==1 or month ==3 or month ==5 or month == 7 or month == 8 or month ==10 or month ==12:
        return 31
    else:
        if month ==2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30

#input1 should befroe the input2
def dateIsBefore(year1,month1,day1,year2,month2,day2):
    if year2>year1:
        return True
    if year2 == year1:
        if month2 > month1:
            return True
        if month2== month1:
            return day2>day1
    return False


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysinMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    days_count = 0
    # program defensively! Add an assertion if the input is not valid!
    # 如果下面這樣寫的話, input1, input2 同一天也會被判斷成 false, 但其實應要回True
    #assert dateIsBefore(year1,month1,day1,year2,month2,day2)

    # 要這樣才當 input1 2 同一天才會對, 因為  dateIsBefore 中 return day2>day1
    # 但我們需要 day2==day1 所以反向來用, 想得到 day2<=day1  的這邊
    assert not dateIsBefore(year2,month2,day2,year1,month1,day1)

    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days_count +=1

    return days_count

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError"),
                  ((2013,1,1,2013,1,1), 0)]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print ("Test case passed!")
            else:
                print ("Test with data:", args, "failed")

        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args))
def mytest():

    #testing case when we implement the helper funs
    assert daysBetweenDates(2013,1,1,2013,1,1) == 0
    assert daysBetweenDates(2013,1,1,2013,1,2) == 1

    #for nextDay and for daysinMonth()
    assert nextDay(2013,1,1) == (2013,1,2)
    assert nextDay(2013,4,30) == (2013,5,1)
    assert nextDay(2012,12,31) == (2013,1,1)
    assert nextDay(2012,2,28) == (2012,2,29)

    #test between days over one years with leap year
    assert isLeapYear(2012)==True
    assert isLeapYear(2013)==False

    assert daysBetweenDates(2013,1,1,2014,1,1) == 365
    assert daysBetweenDates(2012,1,1,2013,1,1) == 366
    assert daysBetweenDates(2013,1,24,2013,6,29) == 156#最一開始的題目



    print('test end')






mytest()
