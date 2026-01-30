max_threshold_number = 100 # max_threshold_number is the number we want to become greater than in our loop
product_number = 1 # both product number and multiplication number start out as normal ones but increase further
multiplication_number = 1

while max_threshold_number > product_number: # while our threshold number is greater than the product number it will 
    # continue to loop
    product_number = product_number * multiplication_number # it multiplies the current product number by our multiplication number
    # which updates the current value of product number
    multiplication_number += 1 # increases the value of the multiplier number by 1 each time it loops
    
print("Final product " + str(product_number)) # lastly, it outputs the final product number and the current multiplication number
print("Final current number: " + str(multiplication_number))
