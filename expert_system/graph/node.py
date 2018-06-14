# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    node.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:21:56 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:55:49 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Node:
  """Node

  Attributes
  ----------
  _type:
    Node type
  _value: boolean
    Does the node requirement are met
  _nodes: list of Node
    All relation node for this node
  """
  def __init__(self):
    self._type = "Node"
    self._value = False
    self._nodes = []

  def __bool__(self):
    return self._value

  def activate(self):
    self._value = True

  def desactivate(self):
    self._value = False

  @property
  def node_type(self):
      return self._type
