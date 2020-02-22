def is_it_summer_yet(threshold_temp, day1_temp, day2_temp, day3_temp):
    number_of_days_threshold = 2  # This is an arbitrary number defined by the exercise
    days_above_temp_threshold = (day1_temp > threshold_temp) +\
                                (day2_temp > threshold_temp) +\
                                (day3_temp > threshold_temp)

    if days_above_temp_threshold >= number_of_days_threshold:
        return True
    else:
        return False
