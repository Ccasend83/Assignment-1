from random import random

random_list_values_between_zero_and_one = [random() for i in range(20)]
random_single_number_between_zero_and_one = random()
list_of_indices_that_contain_values_greater_than = []

sorted_listed_values_between_zero_and_one = sorted(random_list_values_between_zero_and_one)

for indiviual_number_in_sorted_list in sorted_listed_values_between_zero_and_one:
    if indiviual_number_in_sorted_list >= random_single_number_between_zero_and_one:
        list_of_indices_that_contain_values_greater_than.append(indiviual_number_in_sorted_list)

print(f"Sorted list: \n{list_of_indices_that_contain_values_greater_than} \nValue of x: "
      f"\n{random_single_number_between_zero_and_one} \nFirst matching index: "
      f"\n{list_of_indices_that_contain_values_greater_than[0]}")