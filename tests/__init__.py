# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 22:15:47 by kcosta           #+#    #+#              #
#    Updated: 2018/06/16 11:33:35 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import tests.test_core as core
import tests.test_node as node
import tests.test_parser as parser

# print("----------------- Scanner Test -----------------")
# parser.scanner_failed_test()
# parser.scanner_test()

# print("\n-----------------  Lexer Test  -----------------")
# parser.lexer_failed_test()
# parser.lexer_test()

print("\n----------------- Parser Test  -----------------")
parser.parser_test()

# print("\n-----------------  Node  Test  -----------------")
# node.node_easy_test()
# node.node_hard_test()
