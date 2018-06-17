# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    fact_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 23:55:44 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 19:31:53 by kcosta          ###   ########.fr        #
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

  def __str__(self):
    return self.name

  def evaluate(self, origin):
    """Evaluate all attached nodes to activate them when requirements are met

    Parameters
    ----------
    origin: list of Node
      List of already parse node

    Returns
    -------
    True of False
    """
    if bool(self):
      return bool(self)

    origin.append(self)
    for node in self._nodes:
      if node not in origin:
        if node.evaluate(origin):
          self.activate(True)

    return bool(self)
