def calculate_mathematical_expression(number_1, number_2, expression):
    if expression == "-":
        return number_1 - number_2
    elif expression == "+":
        return number_1 + number_2
    elif expression == "/" and number_2 != 0:
        return number_1 / number_2
    elif expression == "*":
        return number_1 * number_2


def calculate_from_string(string):
    number_1, expression, number_2 = string.split()
    number_1, number_2 = float(number_1), float(number_2)
    return calculate_mathematical_expression(number_1, number_2, expression)
