# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    rule_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 23:55:53 by kcosta           #+#    #+#              #
#    Updated: 2018/06/14 23:55:57 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.graph.node import Node


class RuleNode(Node):
  """Node

  Attributes
  ----------
  _not: boolean
    Does the node have the rule NOT
  _and: boolean
    Does the node have the rule AND
  _xor: boolean
    Does the node have the rule XOR
  _or: boolean
    Does the node have the rule OR
  """
  def __init__(self):
    self._type = "Rule"
    self._not = False
    self._and = False
    self._xor = False
    self._or = False

  def setNot(self):
    self._not = True

  def setAnd(self):
    self._and = True

  def setXor(self):
    self._xor = True

  def setOr(self):
    self._or = True
