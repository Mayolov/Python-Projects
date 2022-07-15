# Mayolo Valencia
# displays the time difference in days between the params
def add_time(start, duration, day_of_week = None):
    
    days_of_the_week_dict = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4 , "saturday": 5, "sunday": 6}
    days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # splits the start time and the time of day
    start = start.split()
    
    # splits the start time hrs and min
    start_time =  start[0].split(':')
    
    # start hour as the index 0
    # start hour as index 1
    start_hour = int(start_time[0])
    start_min = int(start_time[1])
    
    # splits the amount of time to add
    # into hrs and min
    duration = duration.split(':')
    
    # duration hour to index 0
    # duration min to idex 1
    duration_hour = int(duration[0])
    duration_min = int(duration[1])

    # gives a place to call the AM or PM
    am_or_pm = start[1]
    
    # searches for the current time of day
    # and returns the opposite value depending
    # on if the time changes
    am_or_pm_flip = {"AM":"PM", "PM":"AM"}
    
    # gives the amount of days thatll pass
    # in the duration
    amount_of_days = duration_hour // 24
    
    # gives the new min
    new_min =  start_min + duration_min
    
    # if the new min is greater than 60
    # add an hour to the start time
    if new_min >= 60:
        
        start_hour += 1
        
        new_min = new_min % 60
    
    # called here so we can properly add to the start time before we add
    # it all together
    new_hour = start_hour + duration_hour
    
    # times itll flip between am or pm
    amount_of_flips = new_hour // 12
    
    # gives the remainder when divided
    new_hour =  new_hour % 12
        
    # if the mins is less than or equal to 9
    # add a 0 infront of new min to make
    # the time look right
    if new_min <= 9:
        new_min = '0' + str(new_min)
        
    # if when the new hours remainder is 0
    # equal it to 12 because 0 means midnight
    # or noon
    if new_hour == 0:
        
        new_hour = 12
    
    # if the start time start with PM and the start time + duration
    # is greater than or equal to 12 add to the number of days that have gone by
    if am_or_pm == "PM" and start_hour + (duration_hour % 12) >= 12:
        
        amount_of_days += 1
       
    # if the amount of flips is odd
    # it will get get the opposite of whatever
    # time of day it is
    if amount_of_flips % 2 == 1:
        
        am_or_pm = am_or_pm_flip[am_or_pm]
    
    # this is the base string of the new time and the time
    # of day
    new_time = str(new_hour) + ':' + str(new_min) + ' ' + am_or_pm
    
    # if there is a day as a 3rd arguement in the parameters
    # this will get the day of the week
    if(day_of_week):
        
        # to make the day uniform and usuable this makes the "
        # arguement lowerase
        day_of_week = day_of_week.lower()
        
        # this gets the index number of whatever day it is
        # this looks in the dictionary for the value of the input day adds
        # the amount of days passed then gets the remainder by 7 to get
        # what day the new time lands on
        index = int((days_of_the_week_dict[day_of_week]) + amount_of_days) % 7
        
        # this gets the total value for the day and finds that index in the array
        new_day = days_of_the_week_array[index]
        
        # this is whats added to the string
        new_time += ", " + new_day
    
    # if the amount of days that pass is just 1
    if amount_of_days == 1:
        
        return new_time + ' ' + '(next day)'
    
    # if the amount of days that pass is more than 1
    elif amount_of_days > 1:
        
        return new_time + ' (' + str(amount_of_days) + " days later)"
    
    return  new_time

def main():
    
    print(add_time("12:00 PM", "1112:00"))
    
main()