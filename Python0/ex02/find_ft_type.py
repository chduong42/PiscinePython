# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/06 19:34:59 by chduong           #+#    #+#              #
#    Updated: 2023/09/06 19:44:04 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List :", type(object))
    elif isinstance(object, tuple):
        print("Tuple :", type(object))
    elif isinstance(object, set):
        print("Set :", type(object))
    elif isinstance(object, dict):
        print("Dict :", type(object))
    elif isinstance(object, str):
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
    
    return 42
