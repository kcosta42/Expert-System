# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    parser.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:30 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:12:06 by kcosta          ###   ########.fr        #
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
  """
  def __init__(self, filename):
    self._lexer = Lexer(filename)

  def parse(self):
    try:
      self._lexer.lexer()
    except Exception as e:
      print("{}".format(e))
      exit(-2)
