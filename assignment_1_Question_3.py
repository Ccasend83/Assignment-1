def taking_number_x_to_the_power_of_y(base_argument_number_x, power_argument_number_y): # simple function that takes in two values and returns the product
    # of taking one value to the power of the other (ex: x and y)
    return base_argument_number_x ** power_argument_number_y

unsorted_number_pairs_list = [[5, 2], [3, -1], [4, 3], [2, 0]] # this is the list of paired numbers we are feeding into our function
list_results_with_no_negative_y_values = [] # this is merely just a empty list that we will use to add our function's product

for argument_number_x, argument_number_y in unsorted_number_pairs_list: # this for loop goes into our unsorted_number_pairs_list and pulls out each specific index slot 0 and 1
    # for each pairs of numbers
    if argument_number_y < 0: # if value at index 1 is less than 0 then we disregard it and move past it
        continue
    sorted_results_list = taking_number_x_to_the_power_of_y(argument_number_x, argument_number_y) # if our initial if statement was not triggered we store the product of out function
    # into a new variable just so we can append it later to our fully sorted list with no negative integers
    list_results_with_no_negative_y_values.append(sorted_results_list)

print(list_results_with_no_negative_y_values) # lastly, it will print the results and sorted values from our final list
