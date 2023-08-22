import re

list_of_number = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890",
    "1-ab2-456-7890",
    "+1 343 303 6668"
]

# Regular expression to match phone numbers
regex = r'\+?\(?\d{0,3}\)?[\s\-.]?\d{3}[\s\-.]?\d{3}[\s\-.]?\d{4}'

# Function to match and filter mobile numbers
def match_mobile_numbers(numbers):
    matching_numbers = [number for number in numbers if re.match(regex, number)]
    return matching_numbers

matching_mobile_numbers = match_mobile_numbers(list_of_number)
print(matching_mobile_numbers)
