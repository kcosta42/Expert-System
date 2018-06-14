# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    token.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:46 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:27:11 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Token:
  """Token

  Parameters
  ----------
  type : number
    Token type
  char : char
    First character of token representation

  Attributes
  ----------
  _value: string
    Token string representation
  """

  def __init__(self, type):
    self.type = type
    self._value = ''

  def __str__(self):
    return '<Token {}> : "{}"'.format(self.type, self._value)

  def __add__(self, other):
    self._value = self._value + other
    return self

TOKEN_TYPE = {
  "EOF": 0,
  "Comment": 1,
  "Whitespace": 2,
  "Newline": 3,
  "Symbol": 4,
  "Fact": 5,
}
