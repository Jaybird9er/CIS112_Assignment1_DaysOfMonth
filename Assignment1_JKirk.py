"""
Author: Jamey Kirk
Date: 03/04/2021
Assignment: Find number of days in a month
Description: Program takes a given month and year and returns the number of days in that month.
"""

def findingLeapYear (year):
    """
    determines if it's a leap year
    """
    leapYear = False
    if year % 4 != 0:
        leapYear = False
    elif year % 100 != 0:
        leapYear = True
    elif year % 400 != 0:
        leapYear = False
    else:
        leapYear = True
    return leapYear

def findingDaysInAMonth (month):
    """
    determines the number of days in the month
    """
    leapYear = findingLeapYear(year)
    if month < 8 and month != 2 and month % 2 == 1:
        return 31
    elif month >= 8 and month % 2 == 0:
        return 31
    elif month == 2 and leapYear == True:
        return 29
    elif month == 2 and leapYear == False:
        return 28
    else:
        return 30

## while loop allows user to repeat the program until they end it
playAgain = True
response = "y"
while playAgain:
    year = int(input("Please enter a 4 digit year: "))
    month = int(input("Please enter the month as (a) digit(s): "))
    findingLeapYear(year)
    print("The month", month, "in year", year, "has", findingDaysInAMonth(month), "days in it.")
    response = input("Do you want to repeat? (Y/N): ")
    if response == "N" or response == "n":
        playAgain = False