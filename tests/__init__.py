# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    __init__.py                                       :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 22:15:47 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 20:55:18 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import tests.test_node as node
import tests.test_parser as parser

print("\n-----------------  Node  Test  -----------------")
node.node_easy_test()
node.node_hard_test()

print("----------------- Scanner Test -----------------")
parser.scanner_failed_test()
parser.scanner_test()

print("\n-----------------  Lexer Test  -----------------")
parser.lexer_failed_test()
parser.lexer_test()

print("\n----------------- Parser Basic Test  -----------------")
parser.parser_basic_test()
print("\n----------------- Parser Hard Test  -----------------")
parser.parser_hard_test()
print("\n----------------- Parser Error Test  -----------------")
parser.parser_error_test()
