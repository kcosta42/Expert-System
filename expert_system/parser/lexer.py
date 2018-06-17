# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    lexer.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 23:15:32 by kcosta          ###   ########.fr        #
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
  _char: chr
    Next character read
  _token: object
    Current Token read

  Exceptions:
  -----------
  OSError if could not open filename
  KeyError if unknown symbol met in file
  """
  def __init__(self, filename):
    self._scan = Scanner(filename)
    self._char = self._scan.read()

  def lexer(self):
    """Lexer function

    Returns
    -------
    _token: object

    Exceptions:
    -----------
    KeyError if unknown symbol met in file
    """
    if not self._char:
      self._token = Token(TOKEN_TYPE['EOF'])
    elif self._char == COMMENT_CHAR:
      self.comment_token()
    elif self._char == NEWLINE_CHAR:
      self.newline_token()
    elif self._char in WHITESPACE_CHARS:
      self.whitespace_token()
    elif self._char in SYMBOL_CHARS:
      self.symbol_token()
    elif self._char in FACT_CHARS:
      self.fact_token()
    else:
      self.raise_KeyError()

    return self._token

  def raise_KeyError(self):
    """Exception KeyError is raised when callling this function"""
    raise KeyError(
      "Unknown symbol '{}' at Ln {}, Col {}".format(self._token,
                                                    self._scan.line,
                                                    self._scan.column)
    )

  def comment_token(self):
    """Set Comment Token"""
    token = Token(TOKEN_TYPE['Comment'])
    while self._char and self._char != NEWLINE_CHAR:
      token = token + self._char
      self._char = self._scan.read()
    self._token = token

  def whitespace_token(self):
    """Set Whitespace Token"""
    token = Token(TOKEN_TYPE['Whitespace'])
    while self._char in WHITESPACE_CHARS:
      token = token + self._char
      self._char = self._scan.read()
    self._token = token

  def symbol_token(self):
    """Set Symbol Token"""
    token = Token(TOKEN_TYPE['Symbol'])
    token = token + self._char
    self._char = self._scan.read()
    if token == '=' and self._char == '>':
      token = token + self._char
      self._char = self._scan.read()
    self._token = token

  def fact_token(self):
    """Set Fact Token"""
    token = Token(TOKEN_TYPE['Fact'])
    token = token + self._char
    self._char = self._scan.read()
    self._token = token

  def newline_token(self):
    """Set Newline Token"""
    token = Token(TOKEN_TYPE['Newline'])
    token = token + self._char
    while self._char == NEWLINE_CHAR:
      self._char = self._scan.read()
    self._token = token
