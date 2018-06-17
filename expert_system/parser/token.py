# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    token.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:46 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 00:25:43 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Token:
  """Token

  Parameters
  ----------
  type : number
    Token type

  Attributes
  ----------
  _value: string
    Token string representation
  _result: boolean
    True if this token is after an Implies Token
    ie. A => B + C
  """

  def __init__(self, type):
    self.type = type
    self._value = ''
    self._result = False

  def __str__(self):
    return '{}'.format(self._value)

  def __add__(self, other):
    self._value = self._value + other
    return self

  def __eq__(self, other):
    return self._value == other

  def clone(self):
    """Return Token clone"""
    token = Token(self.type)
    token._value = self._value
    token._result = self._result
    return token

TOKEN_TYPE = {
  "EOF": 0,
  "Comment": 1,
  "Whitespace": 2,
  "Newline": 3,
  "Symbol": 4,
  "Fact": 5,
}
