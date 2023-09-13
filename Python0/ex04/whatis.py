# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/07 16:45:44 by chduong           #+#    #+#              #
#    Updated: 2023/09/07 20:02:49 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def check_odd_even(number):
    assert isinstance(number, int), "argument is not an integer"
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 1, "more than one argument is provided"
        if len(sys.argv) == 0:
            num = 0
        else:
            num = int(sys.argv[1])
        result = check_odd_even(num)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")