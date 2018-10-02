import os
import random


#Function that generates a random date for the file name
def generate_date(month,year):
    months_31 = [1,3,5,7,8,10,12]
    if month in months_31:
        day = random.randrange(1,30)
    elif month == 2:
        if year % 4 == 0:
            day = random.randrange (1,29)
        else:
            day = random.randrange(1,28)
    else:
        day = random.randrange(1,30)
    return day

    

os.mkdir('files') # make a new directory called files
os.chdir('files') # move to files directory
cities = ['Muscat', 'London', 'Barcelona', 'Salalah', 'Manchester', 'New York'
          , 'Dubai']
