# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/07 14:19:38 by chduong           #+#    #+#              #
#    Updated: 2023/09/07 16:17:44 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math 

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Chesse: {object} {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object} {type(object)}")
    elif isinstance(object, bool) and object == False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found$")
        return 1
    return 0
