# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_parser.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/15 17:39:46 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 23:14:44 by kcosta          ###   ########.fr        #
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
  scan = Scanner('./tests/hard/hard_all')
  os.system('chmod 000 ./tests/hard/hard_all')
  del scan
  os.system('chmod 644 ./tests/hard/hard_all')


def scanner_test():
  scan = Scanner('./tests/hard/hard_all')
  char = scan.read()
  while char:
    print("%c" % char, end="")
    char = scan.read()


def lexer_failed_test():
  try:
    lexer = Lexer('toto')
  except Exception as e:
    print("{}".format(e))
  lexer = Lexer('./tests/hard/hard_all')
  os.system('chmod 000 ./tests/hard/hard_all')
  del lexer
  os.system('chmod 644 ./tests/hard/hard_all')


def lexer_test():
  lexer = Lexer('./tests/hard/hard_all')
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


def parser_basic_test():
  Parser.Verbose = True
  print("Basic")
  parser = Parser('./tests/basic/basic')
  parser.parse()
  print("\n")
  print("Basic AND")
  parser = Parser('./tests/basic/basic_and')
  parser.parse()
  print("\n")
  print("Basic AND Conclusion")
  parser = Parser('./tests/basic/basic_and_conclusion')
  parser.parse()
  print("\n")
  print("Basic NOT")
  parser = Parser('./tests/basic/basic_not')
  parser.parse()
  print("\n")
  print("Basic OR")
  parser = Parser('./tests/basic/basic_or')
  parser.parse()
  print("\n")
  print("Basic Recursion")
  parser = Parser('./tests/basic/basic_recursion')
  parser.parse()
  print("\n")
  print("Basic XOR")
  parser = Parser('./tests/basic/basic_xor')
  parser.parse()
  print("\n")
  print("Basic Biconditional")
  parser = Parser('./tests/basic/basic_biconditional')
  parser.parse()
  print("\n")


def parser_hard_test():
  Parser.Verbose = True
  print("Hard NOT")
  parser = Parser('./tests/hard/hard_not')
  parser.parse()
  print("\n")
  print("Hard OR")
  parser = Parser('./tests/hard/hard_or')
  parser.parse()
  print("\n")
  print("Hard Multiple Conclusion")
  parser = Parser('./tests/hard/multiple_conclusion')
  parser.parse()
  print("\n")
  print("Hard Parentheses")
  parser = Parser('./tests/hard/parentheses')
  parser.parse()
  print("\n")
  print("Hard AND Conclusion")
  parser = Parser('./tests/hard/hard_and_conclusion')
  parser.parse()
  print("\n")
  print("Hard Biconditional")
  parser = Parser('./tests/hard/hard_biconditional')
  parser.parse()
  print("\n")
  print("Hard all")
  parser = Parser('./tests/hard/hard_all')
  parser.parse()
  print("\n")


def parser_error_test():
  Parser.Verbose = True
  try:
    print("Error Contradiction")
    parser = Parser('./tests/error/error_contradiction')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_0')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_1')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_2')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_3')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_4')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_5')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_6')
    parser.parse()
  except Exception as e:
    print(e, end="\n\n")
  try:
    print("Error Syntax")
    parser = Parser('./tests/error/error_syntax_7')
    parser.parse()
  except Exception as e:
    print(e)
