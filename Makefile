# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/12 14:16:09 by kcosta            #+#    #+#              #
#    Updated: 2018/06/12 14:19:05 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

.PHONY: install

install:
	/Users/kcosta/.brew/bin/python3 -m pip install -r requirements.txt
