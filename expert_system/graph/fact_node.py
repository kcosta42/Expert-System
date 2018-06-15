# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    fact_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 23:55:44 by kcosta           #+#    #+#              #
#    Updated: 2018/06/15 17:06:37 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.graph.node import Node, NODE_TYPE


class FactNode(Node):
  """Fact Node

  Parameters
  ----------
  name: string
    Node's name
  """
  def __init__(self, name):
    super().__init__(NODE_TYPE['Fact'])
    self.name = name

  def trigger(self):
    """Trigger all attached nodes to activate them when requirements are met

    Returns
    -------
    True of False
    """
    if bool(self):
      return bool(self)

    for node in self._nodes:
      if node.trigger():
        self.activate(True)

    return bool(self)
