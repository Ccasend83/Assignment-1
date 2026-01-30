import math # imported the math to use pi function in calculations

def circle_area_ratio_calculator(radius_of_circle_one, radius_of_circle_two): # function to calculate both the circle area of both circles and overlay the smaller circle
    # over the bigger circle to find the ratio of the smaller circle covering the bigger circle

    if radius_of_circle_one <= 0 or radius_of_circle_two <= 0: # catches invalid inputs like a radius that is less than or equal to 0
        return "Error, the radius of the circle must be positive and greater than zero."

    circle_one_area = math.pi * radius_of_circle_one ** 2 # calculates the area of both circles
    circle_two_area = math.pi * radius_of_circle_two ** 2

    smaller_area_of_the_two_circles = min(circle_one_area, circle_two_area) # finds the smaller circle and the bigger circle
    larger_area_of_the_two_circles = max(circle_one_area, circle_two_area) # saves them into the corresponding variables

    ratio_of_both_circles_compared_to_one_another = (smaller_area_of_the_two_circles / larger_area_of_the_two_circles) * 100 
    # gets the ratio of the smaller circle over the bigger circle
    # returns a percentage

    return f"{ratio_of_both_circles_compared_to_one_another}%"

print(circle_area_ratio_calculator(9, 10))
