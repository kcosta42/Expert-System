# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    fact_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 23:55:44 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:55:46 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.graph.node import Node


class FactNode(Node):
  """Fact Node

  Parameters
  ----------
  name: string
    Node's name
  """
  def __init__(self, name):
    self._type = "Fact"
    self.name = name
