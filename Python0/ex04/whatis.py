# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/07 16:45:44 by chduong           #+#    #+#              #
#    Updated: 2023/09/13 17:51:39 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def check_odd_even(number):
    assert isinstance(number, int), "argument is not an integer"
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            num = int(sys.argv[1])
        elif len(sys.argv) > 2:
            assert False, "more than one argument is provided"
        else:
            exit()
        check_odd_even(num)
    except AssertionError as e:
        print(f"AssertionError: {e}")