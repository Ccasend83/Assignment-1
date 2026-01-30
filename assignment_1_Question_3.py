def taking_number_x_to_the_power_of_y(base_argument_number_x, power_argument_number_y):
    return base_argument_number_x ** power_argument_number_y

unsorted_number_pairs_list = [[5, 2], [3, -1], [4, 3], [2, 0]]
list_results_with_no_negative_y_values = []

for argument_number_x, argument_number_y in unsorted_number_pairs_list:
    if argument_number_y < 0:
        continue
    sorted_results_list = taking_number_x_to_the_power_of_y(argument_number_x, argument_number_y)
    list_results_with_no_negative_y_values.append(sorted_results_list)

print(list_results_with_no_negative_y_values)