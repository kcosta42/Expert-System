# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Scanner.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 12:22:32 by kcosta            #+#    #+#              #
#    Updated: 2018/06/14 12:52:28 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


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
      self._file = open(self.filename, "rb")
    except IOError as e:
      print("%s" % e)
      exit()

  def __del__(self):
    if (self._file):
      self._file.close()

  def read(self):
    """Read one 8bits character in file"""
    byte = self._file.read(1)

    if (byte == b"\n"):
      self._line += 1
      self._column = 0
      byte = self._file.read(1)

    self._column += 1
    return byte
