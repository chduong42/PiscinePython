# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chduong <chduong@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/06 19:10:30 by chduong           #+#    #+#              #
#    Updated: 2023/09/06 19:28:33 by chduong          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

# Get the current timestamp
timestamp = time.time()
print(timestamp)

# Format the timestamp in the specified way
formatted_timestamp = "{:,.4f} or {:.2e} in scientific notation".format(timestamp, timestamp)

# Get the current date in the specified format
formatted_date = time.strftime("%b %d %Y", time.gmtime())

# Print the formatted output
print("Seconds since January 1, 1970:", formatted_timestamp)
print(formatted_date)