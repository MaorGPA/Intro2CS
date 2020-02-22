def quadratic_equation(a, b, c):
    """ Solves a quadratic equation in form of: a * (x ** 2) + (b * x) + c = 0

    Parameters:
        a (float): the first coefficient.
        b (float): the second coefficient.
        c (float): the third coefficient.

    Returns:
        quadratic_equation(a, b, c): a tuple in length two that holds the solution.
    """
    a_doubled = 2 * a
    discriminant = (b ** 2) - (2 * a_doubled * c)

    if discriminant == 0:
        x1 = -b / a_doubled
        x2 = None
    elif discriminant > 0:
        discriminant_square_root = discriminant ** 0.5
        x1 = (-b + discriminant_square_root) / a_doubled
        x2 = (-b - discriminant_square_root) / a_doubled
    else:
        x1 = x2 = None

    return x1, x2


def quadratic_equation_user_input():
    a, b, c = input("Insert coefficients a, b and c: ").split()
    x1, x2 = quadratic_equation(float(a), float(b), float(c))

    if x1 is None:
        print("The equation has no solutions")
    elif x2 is None:
        print("The equation has 1 solution:", x1)
    else:
        print("The equation has 2 solutions:", x1, "and", x2)
