# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 22:15:47 by kcosta           #+#    #+#              #
#    Updated: 2018/06/13 22:57:46 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import tests.test_core as test_core

assert(test_core.easy_test() == 'Hello')
assert(test_core.easy_test() == 'Helo')
