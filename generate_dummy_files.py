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


#Function that generates a random time for the file name
def generate_time():
    hour = random.randrange(0,23)
    if hour < 10:
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    minutes = random.randrange(0,59)
    if minutes < 10:
        minutes = '0'+str(minutes)
    else:
        minutes = str(minutes)
    seconds = random.randrange(0,59)
    if seconds < 10:
        seconds = '0'+str(seconds)
    else:
        seconds = str(seconds)
    return '_' + hour + minutes + seconds


os.mkdir('files') # make a new directory called files
os.chdir('files') # move to files directory
cities = ['Muscat', 'London', 'Barcelona', 'Salalah', 'Manchester', 'New York'
          , 'Dubai']

index = 0
while index < 150:
    city_name = random.choice(cities)
    year = random.randrange(2009,2017)
    month = random.randrange(1,12)
    day = generate_date(month,year)
    start = str(year)+str(month)+str(day)+"_"
    end = generate_time()
    file_name = start+city_name+end
    f = open(file_name+'.txt','w+') # create a new file
    f.close() # close created file
    index += 1
