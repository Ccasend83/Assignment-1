def create_dictionary_of_strings(listed_strings):
    dictionary_of_strings_that_are_odd_or_even = {}

    for individual_string_in_list in listed_strings:
        length_of_each_string = len(individual_string_in_list)
        if length_of_each_string % 2 == 0:
            parity_of_each_string = "even"
        else:
            parity_of_each_string = "odd"
        dictionary_of_strings_that_are_odd_or_even[individual_string_in_list] = {"length": length_of_each_string,"parity": parity_of_each_string}

    return dictionary_of_strings_that_are_odd_or_even

input_list_of_strings = ["data", "science"]
output_list_of_strings = create_dictionary_of_strings(input_list_of_strings)
print(output_list_of_strings)