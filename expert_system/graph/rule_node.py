# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    rule_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 23:55:53 by kcosta           #+#    #+#              #
#    Updated: 2018/06/15 17:06:18 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.graph.node import Node, NODE_TYPE


class RuleNode(Node):
  """Node

  Parameters
  ----------
  rule: number
    Relation rule between this node and his neighbours
  """
  def __init__(self, rule):
    super().__init__(NODE_TYPE['Rule'])
    self.rule = rule

  def trigger(self):
    """Trigger all attached nodes to activate them when requirements are met

    Returns
    -------
    True or False
    """
    if bool(self):
      return bool(self)

    if self.rule == RELATIONS_RULES['!'] or self.rule == RELATIONS_RULES['=>']:
      self.activate(self._nodes[0].trigger())

    elif self.rule == RELATIONS_RULES['+']:
      count = 0
      for node in self._nodes:
        if not node.trigger():
          count += 1
      if count != 0:
        self.activate(False)
      else:
        self.activate(True)

    elif self.rule == RELATIONS_RULES['|']:
      for node in self._nodes:
        if node.trigger():
          self.activate(True)

    elif self.rule == RELATIONS_RULES['^']:
      count = 0
      for node in self._nodes:
        if node.trigger():
          count += 1
      if count != 1:
        self.activate(False)
      else:
        self.activate(True)

    return bool(self)

RELATIONS_RULES = {
  '!': 0,
  '+': 1,
  '^': 2,
  '|': 3,
  '=>': 4,
}
