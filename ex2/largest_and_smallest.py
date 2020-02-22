def largest_and_smallest(number_1, number_2, number_3):
    number_1_greater_number_2 = number_1 >= number_2
    number_1_greater_number_3 = number_1 >= number_3
    number_2_greater_number_3 = number_2 >= number_3

    if number_1_greater_number_2:
        if number_2_greater_number_3:
            largest, smallest = number_1, number_3
        elif number_1_greater_number_3:
            largest, smallest = number_1, number_2
        else:
            largest, smallest = number_3, number_2
    elif number_2_greater_number_3:
        if number_1_greater_number_3:
            largest, smallest = number_2, number_3
        else:
            largest, smallest = number_2, number_1
    else:
        largest, smallest = number_3, number_1

    return largest, smallest

