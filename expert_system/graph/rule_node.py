# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    rule_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 23:55:53 by kcosta           #+#    #+#              #
#    Updated: 2018/06/16 12:56:11 by kcosta          ###   ########.fr        #
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

  def __str__(self):
    return RULES_STR[self.rule]

  def evaluate(self, origin):
    """Evaluate all attached nodes to activate them when requirements are met

    Returns
    -------
    True or False
    """
    if bool(self) or origin == self:
      return bool(self)

    if self.rule == RELATIONS_RULES['!']:
      self.activate(not self._nodes[0].evaluate(origin))

    elif self.rule == RELATIONS_RULES['=>']:
      self.activate(self._nodes[0].evaluate(origin))

    elif self.rule == RELATIONS_RULES['+']:
      count = 0
      for node in self._nodes:
        if not node.evaluate(origin):
          count += 1
      self.activate(count == 0)

    elif self.rule == RELATIONS_RULES['|']:
      for node in self._nodes:
        if node.evaluate(origin):
          self.activate(True)

    elif self.rule == RELATIONS_RULES['^']:
      count = 0
      for node in self._nodes:
        if node.evaluate(origin):
          count += 1
      self.activate(count == 1)

    return bool(self)

RELATIONS_RULES = {
  '(': -2,
  ')': -1,
  '<=>': 0,
  '=>': 1,
  '^': 2,
  '|': 3,
  '+': 4,
  '!': 5,
}

RULES_STR = {
  1: 'Implies',
  2: 'XOR',
  3: 'OR',
  4: 'AND',
  5: 'NOT',
}
