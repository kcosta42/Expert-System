# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    lexer.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:41:49 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.parser.scanner import Scanner
from expert_system.parser.token import Token, TOKEN_TYPE

COMMENT_CHAR = '#'
WHITESPACE_CHARS = "\t\n\v\f\r "
NEWLINE_CHAR = '\n'
SYMBOL_CHARS = "+()!^|=>?"
FACT_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Lexer:
  """Lexer

  Parameters
  ----------
  filename: string
    Name of the file to be parse

  Attributes
  ----------
  _scan: object
    Scanner object for parsing the file
  """
  def __init__(self, filename):
    self._scan = Scanner(filename)
    self._char = self._scan.read()

  def lexer(self):
    """Lexer function

    Returns
    -------
    token: object
    """
    if not self._char:
      return Token(TOKEN_TYPE['EOF'])
    elif self._char == COMMENT_CHAR:
      return self.comment_token()
    elif self._char == NEWLINE_CHAR:
      return self.newline_token()
    elif self._char in WHITESPACE_CHARS:
      return self.whitespace_token()
    elif self._char in SYMBOL_CHARS:
      return self.symbol_token()
    elif self._char in FACT_CHARS:
      return self.fact_token()
    else:
      raise Exception(
        "Unknown symbol '{}' at Ln {}, Col {}".format(self._char,
                                                      self._scan.line,
                                                      self._scan.column)
      )

  def comment_token(self):
    """Return Comment Token"""
    token = Token(TOKEN_TYPE['Comment'])
    while self._char and self._char != NEWLINE_CHAR:
      token = token + self._char
      self._char = self._scan.read()
    return token

  def whitespace_token(self):
    """Return Whitespace Token"""
    token = Token(TOKEN_TYPE['Whitespace'])
    while self._char in WHITESPACE_CHARS:
      token = token + self._char
      self._char = self._scan.read()
    return token

  def symbol_token(self):
    """Return Symbol Token"""
    token = Token(TOKEN_TYPE['Symbol'])
    token = token + self._char
    self._char = self._scan.read()
    return token

  def fact_token(self):
    """Return Fact Token"""
    token = Token(TOKEN_TYPE['Fact'])
    token = token + self._char
    self._char = self._scan.read()
    return token

  def newline_token(self):
    """Return Newline Token"""
    token = Token(TOKEN_TYPE['Newline'])
    token = token + self._char
    while self._char == NEWLINE_CHAR:
      self._char = self._scan.read()
    return token
