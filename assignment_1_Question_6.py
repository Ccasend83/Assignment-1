def list_of_numbers_to_sorted_dictionary_and_percentages(passed_in_list_of_numbers): # function that takes in a passed in list
    # sorts the values of the list, 
    sorted_dictionary_of_element_percentages = {} # empty dictionary that we will use to store our final values
    elements_in_passed_in_list = len(passed_in_list_of_numbers) # length of the list passed list

    sorted_passed_in_list_of_numbers = sorted(passed_in_list_of_numbers) # after that we sort our list into lowest to greatest
    for individual_number_in_list in sorted_passed_in_list_of_numbers: # for loop that grabs each number from our sorted list that we passed in
        # it doesn't do much but only really exists to loop the nested for loop for each element in the list and to sort out how specific ratios
        elements_less_than_or_equal_to_number = 0

        for current_number_comparison_for_other_values_in_list in sorted_passed_in_list_of_numbers: # this nested loop is similar to the one above however this is where we
            # store our and compare our ratios to other numbers in the list
            if current_number_comparison_for_other_values_in_list <= individual_number_in_list: # while going through the numbers if the we currently have stored in 
                #current_number_comparison_for_other_values_in_list is less than or equal to the specific individual number we grabbed originally it records it in 
                # elements_less_than_or_equal_to_number
                elements_less_than_or_equal_to_number += 1
        ratio_of_elements_less_than_or_equal_to = str(elements_less_than_or_equal_to_number / elements_in_passed_in_list * 100) + "%" # this line 
        # is responsible for creating the ratio percentrage of numbers less than or equal to a specific unique number

        if individual_number_in_list not in sorted_dictionary_of_element_percentages: # this if statement makes sure create and add the unique numerical keys 
            # and ratio values to the dictionary sorted_dictionary_of_element_percentages
            sorted_dictionary_of_element_percentages[individual_number_in_list] = ratio_of_elements_less_than_or_equal_to


    return sorted_dictionary_of_element_percentages

select_initial_numbers = [3, 1, 2, 3, 4, 2] # example initial list
print(list_of_numbers_to_sorted_dictionary_and_percentages(select_initial_numbers))
