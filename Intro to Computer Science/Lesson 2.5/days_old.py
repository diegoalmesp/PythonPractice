# -*- coding: cp1252 -*-
# Given your birthday and the current date, calculate your age in days. 
# Compensate for leap days. 
# Assume that the birthday and current date are correct dates (and
# no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year.

# global daysOfMonths
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# calculation of the days from the starting year
def days_actual_year(y1, m1, d1):
    last_month = daysOfMonths[m1]

    suma = 0
    suma = suma - last_month

    for d in daysOfMonths[:m1 - 1]:
        suma = suma + d

    print "días de " + str(y1) + ": " + str(suma)
    return suma

# calculation of the days from the born year
def days_born_year(y2, m2, d2):
    last_month = daysOfMonths[m2]

    suma = 0
    suma = suma - last_month

    for d in daysOfMonths[m2 + 1:]:
        suma = suma + d

    print "días de " + str(y2) + ": " + str(suma)
    return suma

#################
# main function #
#################
def days_old(y1, m1, d1, y2, m2, d2):
    d1 = days_actual_year(y1, m1, d1)
    d2 = days_born_year(y2, m2, d2)

    respuesta = d1 + d2
    y1 = y1 - 1
    y2 = y2 + 1

    # leap-year count
    count = 2

    while y1 >= y2:
        if count == 4:
            respuesta = respuesta + 1
            count = 1
            print "Year: " + str(y1)
            print "Adding 1 day"
        else:
            count = count + 1
            print "Actual count: " + str(count)

        for d in daysOfMonths:
            respuesta = respuesta + d
            # print d

        # print "actual: " + str(y1)
        y1 = y1 - 1

    print str(respuesta)

# function call
days_old(2015, 6, 13, 1985, 4, 8)
