# Mayolo Valencia
# reads from a file that has previous weather information
# and displays the weather for the day the user asks.

def create_dict():
    with open("weather.txt") as fhandle:
            
        weather_dict = {}
        for line in fhandle:
                
            weather_entries = line.strip().split(';')

            weather_dict[weather_entries[0]] = weather_entries[1:]
    
    return weather_dict

def average(weather_dict):
    
    low_sum = 0
    
    high_sum = 0
    
    for line in create_dict():
        
        low_sum += float(weather_dict.get(line)[2])
        
        high_sum += float(weather_dict.get(line)[1])
    
    large_sum = high_sum / len(weather_dict)
    
    small_avg = low_sum / len(weather_dict)
    
    return small_avg, large_sum

    
def main():
    TOTAL_ENTRIES = len(create_dict())
    
    print("# of entries:", TOTAL_ENTRIES)
    
    print(format(average(create_dict())[0],'.1f'))
    
    print(format(average(create_dict())[1],'.1f'))
    
    user_prompt = False 
       
    while not user_prompt:
        
        date_input = input('Enter date in form yyyy-mm-dd: ')

        if date_input is not "":
            
            if date_input in create_dict():
                
                weather = create_dict().get(date_input)
                
                print(f'{date_input} ({weather[0]}) Low {weather[1]}\u00b0 High {weather[2]}\u00b0') 
            
            else:
                
                print(date_input, 'is not in the weather data.')
                
        else:
            user_prompt = True
main()
