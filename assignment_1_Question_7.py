def seconds_after_midnight_converter(time_in_seconds_after_midnight):
    if time_in_seconds_after_midnight < 0 or time_in_seconds_after_midnight > 86399:
        return "Please input a valid time between 0 and 86399 seconds after the midnight."

    time_in_minutes_after_midnight = 0
    time_in_hours_after_midnight = 0
    specific_time_period_after_midnight = "AM"

    while time_in_seconds_after_midnight >= 60:
        time_in_minutes_after_midnight += 1
        time_in_seconds_after_midnight -= 60
        while time_in_minutes_after_midnight >= 60:
            time_in_hours_after_midnight += 1
            time_in_minutes_after_midnight -= 60
            if time_in_hours_after_midnight > 12 and specific_time_period_after_midnight == "AM":
                specific_time_period_after_midnight = "PM"
            elif time_in_hours_after_midnight > 12 and specific_time_period_after_midnight == "PM":
                specific_time_period_after_midnight = "AM"

    return (f"{time_in_hours_after_midnight} {time_in_minutes_after_midnight} {time_in_seconds_after_midnight} "
            f"{specific_time_period_after_midnight}")



initial_time_in_seconds_after_midnight = 19067
#initial_time_in_seconds_after_midnight = 86400
#initial_time_in_seconds_after_midnight = -1
#initial_time_in_seconds_after_midnight = 50000
print(seconds_after_midnight_converter(initial_time_in_seconds_after_midnight))