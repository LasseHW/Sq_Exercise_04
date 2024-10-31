import math

def calculate_area(shape, *args):
    if shape == "circle" and len(args) == 1:
        return math.pi * args[0] ** 2
    elif shape == "square" and len(args) == 1:
        return args[0] ** 2
    elif shape == "rectangle" and len(args) == 2:
        return args[0] * args[1]
    else:
        raise ValueError("Invalid shape or arguments.")
