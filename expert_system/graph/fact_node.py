# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fact_node.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 10:59:27 by kcosta            #+#    #+#              #
#    Updated: 2018/06/14 11:58:58 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


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
