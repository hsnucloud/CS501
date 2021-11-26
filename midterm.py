# midterm.py
"""
This midterm.py is for the midterm from CS 501 class
Student's name: Chien-Hsien Lin
PUID: 0031982200
"""
# Import modules
from functools import reduce
import pandas as pd
import re

# ======================================================================================================================

# Problem 1
def q1():
    """
        q1() function implements finding a list of difference and its sum
    """
    # Input p and q set
    while True:
        try:
            p = input("Enter the p list and separate the integers with ',': ")
            p = {int(x.strip()) for x in p.split(',')}
        except:
            print("NOTICE: Enter integers only and separate them with ','. Please input again.")
        else:
            break
    while True:
        try:
            q = input("Enter the q list and separate the integers with ',': ")
            q = {int(x.strip()) for x in q.split(',')}
        except:
            print("NOTICE: Enter integers only and separate them with ','. Please input again.")
        else:
            break
    # Finding r list which has elements different from q in p
    r = p - q
    r = list(r)
    # Print out r and sum
    if r:
        for x in r:
            print(x, end=' ')
        print('\n', sum(r), sep='')
    else:
        print(None)
# ======================================================================================================================

# Problem 2
def q2():
    """
        q2() function implements finding aircraft without complete maintenance
    """
    # Read the file, am.txt
    with open('am.txt', 'r') as f:
        data = f.readlines()
        n = len(data) # Number of aircraft
    # Split items in data with comma
    data = [data[i].split(',') for i in range(n)]
    # Extract the numbers of maintenance rounds
    rounds = [len(data[i])-1 for i in range(n)]
    # Map for the review
    review = list(map(lambda x: 1 if x == 4 else 0, rounds))
    print("Outcome of maintenance review:", review)
    # Calculate the number of aircraft without complete maintenance
    lack_sum = reduce(lambda a, b: a+b, [1-val for val in review])
    #lack_sum = n - sum(review)
    print("Number of aircraft not maintained for four rounds:", lack_sum)
    # List the aircraft with the years of incomplete maintenance
    full_years = {'2012', '2013', '2014', '2015'}
    for i in range(n):
        if review[i] == 0:
            # Label of the aircraft
            print(data[i][0].rstrip('\n'), end=' ')
            years = set()
            for j in range(rounds[i]):
                y = data[i][j+1].split('.')[2].rstrip('\n') # Year of maintenance
                years.add(y)
            # Derive the lost years
            lack = sorted([int(x) for x in list(full_years - years)])
            # Print the lost years
            for k in lack:
                print(k, end=' ')
            print(end='\n')
# ======================================================================================================================

# Problem 3
def find_open(data_file, date_time:str):
    """
    Read the data file to look for the open restaurants on the specific date and time
    :param data_file: restaurant list
    :param date_time: specific date and time in string
    :return:
    """
    # Convert the specific date_time
    date_time_f = pd.Timestamp(date_time)
    # Load the file
    with open(data_file, 'r') as f:
        data = f.readlines()
        data = [rest.split(',') for rest in data]
    # Dictionary to store restaurants and open time
    data_dict = {
        'names': [],
        'Mon': [],
        'Tue': [],
        'Wed': [],
        'Thu': [],
        'Fri': [],
        'Sat': [],
        'Sun': []
    }
    # Week-days reference
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # The day of specific date
    day = week[date_time_f.dayofweek]
    # Extract information into data_dict
    open_restaurants = [] # Initialize a list of open restaurant
    # Store anc check the available time
    for r, rest_time in enumerate(data):
        # Add restaurants' names
        data_dict['names'].append(rest_time[0])
        open_days = [] # Create a list of open days within the week
        # Parse the open time and days
        for i in range(1, len(rest_time)):
            temp = rest_time[i].strip().split(' ')
            # Find the time
            time = re.findall("\d*.\d+ .m", rest_time[i])
            # Find the week days
            days = temp[0].split('-')
            if len(days) > 1: # A series of days
                s = week.index(days[0]) # Start day of the range
                e = week.index(days[1]) # End day of the range
                open_days += list(range(s, e+1)) # Add into open days
                # Update the data dictionary
                for d in range(s, e+1):
                    data_dict[week[d]].append(time)
            else: # Single day
                d = week.index(days[0])
                open_days.append(d) # Add into open days
                # Update the data dictionary
                data_dict[week[d]].append(time)
        # Check closed days and add an empty list
        for j in range(7):
            if j not in open_days:
                data_dict[week[j]].append([])
        # Specific date
        date = date_time.split()[0]
        # Check if this restaurant is open on the assigned date and time
        if data_dict[day][r]: # Check if the day is open
            start = pd.Timestamp(date + ' ' + data_dict[day][r][0]) # Start of open period
            end = pd.Timestamp(date + ' ' + data_dict[day][r][1]) # End of open period (close time)
            # Check if the time is inside the open period
            if start <= date_time_f <= end:
                open_restaurants.append(data_dict['names'][r])
    # Print the restaurants in alphabetical order
    print(sorted(open_restaurants))

def q3():
    """
        q3() function calls find_open function to search for the restaurants in open time
    """
    find_open('rest_hours.txt', '11/07/2021 09:00 am')

def main():
    q1()
    q2()
    q3()

if __name__ == '__main__':
    main()