# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
def isLeapYear(year):
    leap_year = True
    if year % 4 != 0:
        leap_year = False
    elif year % 100 !=0:
        leap_year = True
    elif year % 400 != 0:
        leap_year = False
    else:
        leap_year = True
    return leap_year
    

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    daysInAYear = 365
    y = y1
    m = m2
    days = (daysOfMonths[m1 - 1] - d1) + d2
    while y < y2:
        y += 1
        if isLeapYear(y):
            days += 1
        if m <= m1:
            days -= daysOfMonths[m - 1]
            m += 1
        days += daysInAYear
    return days
