def seconds_after_midnight_converter(time_in_seconds_after_midnight): # this function primarily exists to convert time in seconds after midnight to hours,
    # minutes, and left over seconds
    # it also changes the time period regarding "AM" or "PM"
    if time_in_seconds_after_midnight < 0 or time_in_seconds_after_midnight > 86399: # this if statement catches any invalid time that the program might  deal with
        # anything less than 0 or greater 86399 will be caught and not registered(86400 is the amount of seconds in a day)
        return "Please input a valid time between 0 and 86399 seconds after the midnight."

    time_in_minutes_after_midnight = 0 # initializing all variables before our main loop
    time_in_hours_after_midnight = 0
    specific_time_period_after_midnight = "AM"

    while time_in_seconds_after_midnight >= 60: # this first while loop makes it so it checks if there is 60 seconds left from the original seconds
        # after midnight
        # if there exists more than or equal to 60 seconds it converts them into 1 time_in_minutes_after_midnight while subtracting 60 from time_in_seconds_after_midnight
        time_in_minutes_after_midnight += 1
        time_in_seconds_after_midnight -= 60
        while time_in_minutes_after_midnight >= 60: # this second while loop catches if time_in_minutes_after_midnight exceedes 60 or more
            # if it does it converts the 60 minutes into 1 hour after midnight
            time_in_hours_after_midnight += 1
            time_in_minutes_after_midnight -= 60
        
            if time_in_hours_after_midnight > 12 and specific_time_period_after_midnight == "AM": # if a total of 12 hours have past since midnight
                # the program changes the specific time period.
                # for example it starts out as "AM" but after 12 hours it changes to "PM"
                specific_time_period_after_midnight = "PM"
            elif time_in_hours_after_midnight > 12 and specific_time_period_after_midnight == "PM": # this elif statement does the exact same thing but another 12 hours passes after midnight
                # this is a little redundant because it's impossible to exceed 86400 seconds after midnight but I thought it would be handy
                specific_time_period_after_midnight = "AM"

    return (f"{time_in_hours_after_midnight} {time_in_minutes_after_midnight} {time_in_seconds_after_midnight} " 
            f"{specific_time_period_after_midnight}")
            # this is the main return statement, it returns the hours, minutes, left over seconds, and time period after midnight


initial_time_in_seconds_after_midnight = 19067 # these are all test cases
#initial_time_in_seconds_after_midnight = 86400
#initial_time_in_seconds_after_midnight = -1
#initial_time_in_seconds_after_midnight = 50000
print(seconds_after_midnight_converter(initial_time_in_seconds_after_midnight))
