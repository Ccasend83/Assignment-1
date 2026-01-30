def list_of_numbers_to_sorted_dictionary_and_percentages(passed_in_list_of_numbers):
    sorted_dictionary_of_element_percentages = {}
    elements_in_passed_in_list = len(passed_in_list_of_numbers)

    sorted_passed_in_list_of_numbers = sorted(passed_in_list_of_numbers)
    for individual_number in sorted_passed_in_list_of_numbers:
        elements_less_than_or_equal_to_number = 0

        for i in sorted_passed_in_list_of_numbers:
            if i <= individual_number:
                elements_less_than_or_equal_to_number += 1
        ratio_of_elements_less_than_or_equal_to = str(elements_less_than_or_equal_to_number / elements_in_passed_in_list * 100) + "%"

        if individual_number not in sorted_dictionary_of_element_percentages:
            sorted_dictionary_of_element_percentages[individual_number] = ratio_of_elements_less_than_or_equal_to


    return sorted_dictionary_of_element_percentages

select_initial_numbers = [3, 1, 2, 3, 4, 2]
print(list_of_numbers_to_sorted_dictionary_and_percentages(select_initial_numbers))