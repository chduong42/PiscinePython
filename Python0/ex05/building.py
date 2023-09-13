# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/13 19:37:35 by chduong           #+#    #+#              #
#    Updated: 2023/09/13 19:48:46 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def calculate_char_sums(input_string):
    upper_case_sum = 0
    lower_case_sum = 0
    punctuation_sum = 0
    digit_sum = 0
    space_sum = 0

    for char in input_string:
        if char.isupper():
            upper_case_sum += 1
        elif char.islower():
            lower_case_sum += 1
        elif char in string.punctuation:
            punctuation_sum += 1
        elif char.isdigit():
            digit_sum += 1
        elif char.isspace():
            space_sum += 1

    return {
        "Upper Case": upper_case_sum,
        "Lower Case": lower_case_sum,
        "Punctuation": punctuation_sum,
        "Digits": digit_sum,
        "Spaces": space_sum,
    }
    
def main ():
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
    elif len(sys.argv) == 1:
        input_string = input("What is the text to count?\n")
    else:
        raise AssertionError("More than one argument is provided")

    char_sums = calculate_char_sums(input_string)

    total_characters = len(input_string)
    print(f"The text contains {total_characters} characters:")

    for category, count in char_sums.items():
        print(f"{count} {category.lower()} letters")

    print(f"{char_sums['Punctuation']} punctuation marks")
    print(f"{char_sums['Spaces']} spaces")
    print(f"{char_sums['Digits']} digits")

if __name__ == "__main__":
    main()