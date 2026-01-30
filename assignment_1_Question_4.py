from random import random # importing random function to get be able to pick out random numbers between 0 and 1

random_list_values_between_zero_and_one = [random() for i in range(20)] # this is our list of randomly generated values
random_single_number_between_zero_and_one = random() # this is our randomly generated "x" variable that we use to compare to our list of random numbers
list_of_indices_that_contain_values_greater_than = [] # this is just an empty list that we will use to store numbers greater than our "x" variable

sorted_listed_values_between_zero_and_one = sorted(random_list_values_between_zero_and_one) # first we sort our randomized list least to greatest

for indiviual_number_in_sorted_list in sorted_listed_values_between_zero_and_one: # this for loop picks out each individual value in our ordered randomized list
    if indiviual_number_in_sorted_list >= random_single_number_between_zero_and_one: # if it finds a number greater than or equal to our randomized "x" variable it stores that
        # number
        list_of_indices_that_contain_values_greater_than.append(indiviual_number_in_sorted_list) # lastly, it appends that value to our currently empty list list_of_indices_that_contain_values_greater_than

print(f"Sorted list: \n{list_of_indices_that_contain_values_greater_than} \nValue of x: " # Finally it outputs our final list "list_of_indices_that_contain_values_greater_than", our "x" variable,
      # and the first matching index that was greater than or equal to our "x" variable
      f"\n{random_single_number_between_zero_and_one} \nFirst matching index: "
      f"\n{list_of_indices_that_contain_values_greater_than[0]}")
