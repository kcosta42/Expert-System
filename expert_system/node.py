# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    node.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/12 13:38:52 by kcosta            #+#    #+#              #
#    Updated: 2018/06/12 14:26:08 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from expert_system.vertex import Vertex

class Node:
  """
    Node

    Parameters:
      name: string

    Attribute:
      _name:    string
      _value:   boolean
      _vertice: list of Vertex
  """
  def __init__(self, name):
    self._name = name
    self._value = False
    self._vertices = []

  def add_vertex(self, dest):
    self._vertices.append( Vertex(self, dest) )
