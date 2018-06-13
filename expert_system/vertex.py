# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    vertex.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:21:21 by kcosta           #+#    #+#              #
#    Updated: 2018/06/13 21:21:44 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Vertex:
  """Vertex direction from two nodes

  Parameters
  ----------
  origin  : Node
    The origin node
  dest    : Node
    The destination node

  Attributes
  ----------
  _not: boolean
    relation NOT between the two node
  """
  def __init__(self, origin, dest):
    self.origin = origin
    self.dest = dest
    self._not = False
