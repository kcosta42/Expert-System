# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vertex.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/12 13:43:18 by kcosta            #+#    #+#              #
#    Updated: 2018/06/12 14:25:55 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vertex:
  """
    Vertex

    Parameters:
      origin: Node
      dest:   Node

    Attribute:
      _not: boolean
  """
  def __init__(self, origin, dest):
    self._origin = origin
    self._dest = dest
    self._not = False
