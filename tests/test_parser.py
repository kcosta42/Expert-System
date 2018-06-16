# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_parser.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/15 17:39:46 by kcosta           #+#    #+#              #
#    Updated: 2018/06/16 13:00:48 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import os

from expert_system.parser.scanner import Scanner
from expert_system.parser.token import TOKEN_TYPE
from expert_system.parser.lexer import Lexer
from expert_system.parser.parser import Parser


def scanner_failed_test():
  try:
    scan = Scanner('toto')
  except Exception as e:
    print("{}".format(e))
  scan = Scanner('./docs/example')
  os.system('chmod 000 ./docs/example')
  del scan
  os.system('chmod 644 ./docs/example')


def scanner_test():
  scan = Scanner('./docs/example')
  char = scan.read()
  while char:
    print("%c" % char, end="")
    char = scan.read()


def lexer_failed_test():
  try:
    lexer = Lexer('toto')
  except Exception as e:
    print("{}".format(e))
  lexer = Lexer('./docs/example')
  os.system('chmod 000 ./docs/example')
  del lexer
  os.system('chmod 644 ./docs/example')


def lexer_test():
  lexer = Lexer('./docs/example')
  try:
    token = lexer.lexer()
    while token.type != TOKEN_TYPE['EOF']:
      if token.type != TOKEN_TYPE['Whitespace']:
        if token.type != TOKEN_TYPE['Comment']:
          if token.type != TOKEN_TYPE['Newline']:
            print('{}'.format(token), end=" ")
          else:
            print()
      token = lexer.lexer()
  except Exception as e:
    print('{}'.format(e))


def parser_test():
  parser = Parser('./docs/basic_and_conclusion')
  parser.parse()
  parser.evaluate_queries()
