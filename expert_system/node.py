# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    node.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:21:56 by kcosta           #+#    #+#              #
#    Updated: 2018/06/13 23:42:14 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.vertex import Vertex


class Node:
  """Node

  Parameters
  ----------
  name: string
    Node's name

  Attributes
  ----------
  _value  : boolean
    Does the node requirement are met
  _vertice: list of Vertex
    All relation vertex for this node
  """
  def __init__(self, name):
    self.name = name
    self._value = False
    self._vertices = []

  def add_vertex(self, dest):
    """Create relation between two node"""
    self._vertices.append(Vertex(self, dest))
