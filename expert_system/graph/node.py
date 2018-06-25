class Node:
  """Node

  Parameters
  ----------
  type: number
    Node type

  Attributes
  ----------
  _activate: boolean
    Does the node requirement are met
  _nodes: list of Node
    All relation node for this node
  """
  def __init__(self, type):
    self.type = type
    self._activate = False
    self._nodes = []

  def __bool__(self):
    return self._activate

  def activate(self, value):
    """Activate node"""
    self._activate = value

  def connect(self, other):
    """Link node to another node"""
    self._nodes.append(other)

  def reset(self, origin):
    """Reset node

    Parameters
    ----------
    origin: list of Node
      List of already parse node
    """
    self._activate = False
    origin.append(self)
    for node in self._nodes:
      if node not in origin:
        node.reset(origin)


NODE_TYPE = {
  "Node": 0,
  "Fact": 1,
  "Rule": 2,
}
