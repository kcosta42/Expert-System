# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    Makefile                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:22:40 by kcosta           #+#    #+#              #
#    Updated: 2018/06/13 23:02:54 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

NAME := expert_system

.PHONY: install test clean

install:
	@python3 -m pip install -r requirements.txt

test:
	@python3 setup.py test || true

clean:
	@python3 setup.py clean
	@rm -rf $(NAME)/__pycache__/	2> /dev/null || true
	@rm -rf tests/__pycache__/		2> /dev/null || true
	@rm -rf $(NAME).egg-info/ 		2> /dev/null || true
