def create_dictionary_of_strings(listed_strings): # this function creates a basic dictionary of strings using a passed in list as the argument
    dictionary_of_strings_that_are_odd_or_even = {} # dictionary_of_strings_that_are_odd_or_even is just the empty dictionary that
    # is being using to keep track of the strings, parity, and length of a string

    for individual_string_in_list in listed_strings: # goes into the passed in list and takes out each individual string found in it
        length_of_each_string = len(individual_string_in_list)
        if length_of_each_string % 2 == 0: # using modulus we can figure out whether a the length of a certain string is odd or even
            # if the modulus of the length is equal to 0 the length is even
            # else it must be odd
            parity_of_each_string = "even"
        else:
            parity_of_each_string = "odd"
        dictionary_of_strings_that_are_odd_or_even[individual_string_in_list] = {"length": length_of_each_string,"parity": parity_of_each_string}
        # it then feeds the sorted string and it's attribrutes into the empty dictionary we initialiazed in the beginning
        # repeats for every string found in the list

    return dictionary_of_strings_that_are_odd_or_even

input_list_of_strings = ["data", "science"]
output_list_of_strings = create_dictionary_of_strings(input_list_of_strings)
print(output_list_of_strings)
