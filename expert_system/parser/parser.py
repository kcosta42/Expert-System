# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    parser.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:30 by kcosta           #+#    #+#              #
#    Updated: 2018/06/15 11:18:13 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.parser.lexer import Lexer


class Parser:
  """Parser

  Parameters
  ----------
  filename: string
    Name of the file to be parse

  Attributes
  ----------
  _lexer: object
    Lexer object for parsing the file

  Exceptions:
  -----------
  OSError if could not open filename
  KeyError if unknown symbol met in file
  """
  def __init__(self, filename):
    self._lexer = Lexer(filename)

  def parse(self):
    self._lexer.lexer()
