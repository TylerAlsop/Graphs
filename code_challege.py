# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

#P
def sum_values():
    # Create a variable for the dictionary.
    given_dictionary = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
    }

    # Create and empty list to hold numerical values.
    list_of_numbers = []

    # dictionary_values = given_dictionary.values()

    # Loop over the dictionary values
    for item in given_dictionary.values():
        # If the value of the item is a number
        if type(item) is int:
            # Add it to the list
            list_of_numbers.append(item)
    # Sum the values in the list (Look up sum method)
    sum_of_numbers = sum(list_of_numbers)

    # Return sum
    return sum_of_numbers

print(sum_values())
