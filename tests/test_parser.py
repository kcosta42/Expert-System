# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_parser.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/15 17:39:46 by kcosta           #+#    #+#              #
#    Updated: 2018/06/15 17:40:02 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import os

from expert_system.parser.scanner import Scanner
from expert_system.parser.lexer import Lexer
from expert_system.parser.token import TOKEN_TYPE


def scanner_failed_test():
  try:
    scan = Scanner('toto')
  except Exception as e:
    print("{}".format(e))
  scan = Scanner('./docs/example.txt')
  os.system('chmod 000 ./docs/example.txt')
  del scan
  os.system('chmod 644 ./docs/example.txt')


def scanner_test():
  scan = Scanner('./docs/example.txt')
  char = scan.read()
  while char:
    print("%c" % char, end="")
    char = scan.read()


def lexer_failed_test():
  try:
    lexer = Lexer('toto')
  except Exception as e:
    print("{}".format(e))
  lexer = Lexer('./docs/example.txt')
  os.system('chmod 000 ./docs/example.txt')
  del lexer
  os.system('chmod 644 ./docs/example.txt')


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
