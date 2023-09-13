# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex00.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/06 17:25:44 by chduong           #+#    #+#              #
#    Updated: 2023/09/06 19:08:37 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.update({"Paris!"})

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)