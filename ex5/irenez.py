test_list = [4, 12, 3, 2, 34, 1, 33, 12, 4, 900, 300, 3, 12, 7]


def maorzsorts(my_list):
    for k in range(1, len(my_list)):
        i = k
        j = i - 1
        while my_list[i] < my_list[j] and i != 0:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i -= 1
            j = i - 1

    return my_list


print(maorzsorts(test_list))
