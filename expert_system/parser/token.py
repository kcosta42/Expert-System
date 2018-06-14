class Token:
  """Token
  
  Parameters
  ----------
  type : number
    Token type
  
  Attributes
  ----------
  """
  
  NONE = 0
  OPERAND = 1
  VARIABLE = 2
  
  def __init__(self, type):
    self.type = type

  @property
  def type(self):
    return self.type