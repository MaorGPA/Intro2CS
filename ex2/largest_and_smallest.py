def largest_and_smallest(number_1, number_2, number_3):
    # This function returns the largest number and then the smallest number out of the three arguments
    number_1_greater_number_2 = number_1 >= number_2
    number_1_greater_number_3 = number_1 >= number_3
    number_2_greater_number_3 = number_2 >= number_3

    if number_1_greater_number_2:
        if number_2_greater_number_3:
            return number_1, number_3
        elif number_1_greater_number_3:
            return number_1, number_2
        else:
            return number_3, number_2
    elif number_2_greater_number_3:
        if number_1_greater_number_3:
            return number_2, number_3
        else:
            return number_2, number_1
    else:
        return number_3, number_1
