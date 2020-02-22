import math


def shape_area():
    # This function calculates and prints the area of a circle, rectangle or trapezoid according to user selection
    user_selection = input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): ")

    if user_selection == "1":
        radius = float(input())
        print(compute_circle_area(radius))
    elif user_selection == "2":
        width = float(input())
        height = float(input())
        print(compute_rectangle_area(width, height))
    elif user_selection == "3":
        leg_a = float(input())
        leg_b = float(input())
        height = float(input())
        print(compute_trapezoid_area(leg_a, leg_b, height))
    else:
        print(None)


def compute_circle_area(radius):
    return math.pi * (radius ** 2)


def compute_rectangle_area(width, height):
    return width * height


def compute_trapezoid_area(leg_a, leg_b, height):
    legs_average = (leg_a + leg_b) / 2
    return legs_average * height
