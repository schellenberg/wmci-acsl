# Navigating ACSLland -- Contest 1 - 2014/15
# check the file contest_demo_input.txt to understand how this works

#known error:
# need to think up a way to fix the floating point roundoff error for 6:42 / 6:43 on test input 1

def process_problem(this_line):
    item_list = this_line.split(", ")
    
    first_starting_city = item_list[0]
    second_starting_city = item_list[1]

    first_starting_time = int(item_list[2])
    first_starting_time_am_pm = item_list[3]

    second_starting_time = int(item_list[4])
    second_starting_time_am_pm = item_list[5]

    first_speed = int(item_list[6])
    second_speed = int(item_list[7])

    total_distance = find_distance_from(first_starting_city, second_starting_city)
    time_difference, starting_traveller = find_time_difference(first_starting_time, first_starting_time_am_pm, second_starting_time, second_starting_time_am_pm)

    if starting_traveller == 1:
        early_bird_distance = time_difference * first_speed
        distance_remaining = total_distance - early_bird_distance

    elif starting_traveller == 2:
        early_bird_distance = time_difference * second_speed
        distance_remaining = total_distance - early_bird_distance
    
    else:
        early_bird_distance = 0
        distance_remaining = total_distance

    dual_travel_time_hours = distance_remaining // (first_speed + second_speed)
    dual_travel_time_minutes = (distance_remaining / (first_speed + second_speed) - dual_travel_time_hours) % 1 * 60

    if starting_traveller == 1:
        total_hours = dual_travel_time_hours + time_difference
    else:
        total_hours = dual_travel_time_hours
    
    # if 

    # https://pyformat.info/#number_padding
    print('{:d}:{:02.0f}'.format(total_hours, dual_travel_time_minutes))

def find_distance_from(city1, city2):
    distance_list = [450, 140, 125, 365, 250, 160, 380, 235, 320]
    location_values = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "J":8, "K":9}

    #remember we will go up to, but not including the ending_spot in the for loop
    starting_spot = location_values[city1]
    ending_spot = location_values[city2] 

    total_distance = 0
    for distance_travelled in distance_list[starting_spot:ending_spot]:
        total_distance += distance_travelled

    return total_distance

def find_time_difference(start_hour1, am_pm1, start_hour2, am_pm2):
    #convert to 24 hour time
    if am_pm1 == "PM" and start_hour1 != 12:
        start_hour1 += 12
    if am_pm2 == "PM" and start_hour2 != 12:
        start_hour2 += 12

    #catch edge case of 12am (midnight)
    if am_pm1 == "AM" and start_hour1 == 12:
        start_hour1 = 0
    if am_pm1 == "AM" and start_hour2 == 12:
        start_hour2 = 0

    time_difference = abs(start_hour1 - start_hour2)
    
    if time_difference > 12:
        if start_hour1 < start_hour2:
            start_hour1 += 24
            time_difference = start_hour1 - start_hour2
            starting_traveller = 2
        else:
            start_hour2 += 24
            time_difference = start_hour2 - start_hour1
            starting_traveller = 1
    else:
        if start_hour1 < start_hour2:
            starting_traveller = 1
        elif start_hour2 < start_hour1:
            starting_traveller = 2
        else:
            starting_traveller = 0

    return time_difference, starting_traveller

########################################################################################################

input_file = open("contest_test_input.txt")

# Loop through every line. Each line is one sample problem.
for line in input_file:
    process_problem(line.strip() )  #strip removes the extra line break

