# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    scanner.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:22 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:40:42 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Scanner:
  """Scan each character in given file

  Parameters:
  -----------
  filename: string
    name of the file to open

  Attributes:
  -----------
  _file   : file
    file opened
  _column : number
    current column in file
  _line   : number
    current line in file
  """
  def __init__(self, filename):
    self.filename = filename
    self._column = 0
    self._line = 1
    try:
      self._file = open(self.filename, "r")
    except IOError as e:
      print("%s" % e)
      exit(-1)

  def __del__(self):
    try:
      self._file.close()
    except:
      pass

  def read(self):
    """Read one 8bits character in file

    Returns
    -------
    char: char
      character read
    """
    char = self._file.read(1)

    if (char == '\n'):
      self._line += 1
      self._column = -1

    self._column += 1
    return char

  @property
  def column(self):
    return self._column

  @property
  def line(self):
    return self._line
