# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_core.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 22:08:43 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:38:49 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.parser.scanner import Scanner
from expert_system.parser.lexer import Lexer
from expert_system.parser.token import TOKEN_TYPE


def scanner_test():
  scan = Scanner('./docs/example.txt')
  char = scan.read()
  while char:
    print("%c" % char, end="")
    char = scan.read()


def lexer_test():
  lexer = Lexer('./docs/example.txt')
  try:
    token = lexer.lexer()
    while token.type != TOKEN_TYPE['EOF']:
      if token.type != TOKEN_TYPE['Whitespace']:
        if token.type != TOKEN_TYPE['Newline']:
          if token.type != TOKEN_TYPE['Comment']:
            print('{}'.format(token))
      token = lexer.lexer()
  except Exception as e:
    print('{}'.format(e))
