import readline
import sys

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')
readline.parse_and_bind('Meta-h: backward-kill-word')
readline.parse_and_bind('"\C-u": universal-argument')
readline.parse_and_bind('set horizontal-scroll-mode On')

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

  Exceptions:
  -----------
  OSError if could not open filename
  """
  def __init__(self, filename):
    self.filename = filename
    self._column = 0
    self._line = 1
    self._file = open(self.filename, "r")
    self._interactive = False
    self._flag = False
    self._input = ";"

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
    if self._interactive:
      return self.read_interative()
  
    char = self._file.read(1)
    if not char:
      self._interactive = True
      self._column = 0
      self._line = 0
      return char

    if (char == '\n'):
      self._line += 1
      self._column = -1

    self._column += 1
    return char
  
  def read_interative(self):
    char = self._input[self._column]

    if char == ';' and not self._flag:
      self._flag = True
      return ' '

    if (char == ';'):
      self._input = input("\n> ") + "\n;"
      self._column = 0
      self._flag = False
      char = self._input[self._column]

    self._column += 1
    return char


  @property
  def column(self):
    return self._column

  @property
  def line(self):
    return self._line
