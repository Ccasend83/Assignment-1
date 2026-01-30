max_threshold_number = 100
product_number = 1
multiplication_number = 1

while max_threshold_number > product_number:
    product_number = product_number * multiplication_number
    multiplication_number += 1
print("Final product " + str(product_number))
print("Final current number: " + str(multiplication_number))