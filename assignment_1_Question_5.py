import math

def circle_area_ratio_calculator(radius_of_circle_one, radius_of_circle_two):

    if radius_of_circle_one <= 0 or radius_of_circle_two <= 0:
        return "Error, the radius of the circle must be positive and greater than zero."

    circle_one_area = math.pi * radius_of_circle_one ** 2
    circle_two_area = math.pi * radius_of_circle_two ** 2

    smaller_area_of_the_two_circles = min(circle_one_area, circle_two_area)
    larger_area_of_the_two_circles = max(circle_one_area, circle_two_area)

    ratio_of_both_circles_compared_to_one_another = (smaller_area_of_the_two_circles / larger_area_of_the_two_circles) * 100

    return f"{ratio_of_both_circles_compared_to_one_another}%"

print(circle_area_ratio_calculator(9, 10))