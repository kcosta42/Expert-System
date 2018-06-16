# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    node.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:21:56 by kcosta           #+#    #+#              #
#    Updated: 2018/06/16 02:12:46 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


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
    self._activate = value

  def connect(self, other):
    self._nodes.append(other)

  def reset(self):
    for node in self._nodes:
      node.reset()
    self._activate = False


NODE_TYPE = {
  "Node": 0,
  "Fact": 1,
  "Rule": 2,
}
