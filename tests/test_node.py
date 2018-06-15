# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_node.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/15 17:40:14 by kcosta           #+#    #+#              #
#    Updated: 2018/06/15 17:40:18 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.graph.rule_node import RuleNode, RELATIONS_RULES
from expert_system.graph.fact_node import FactNode


def node_easy_test():
  fA = FactNode('A')
  fB = FactNode('B')
  fC = FactNode('C')
  rAnd = RuleNode(RELATIONS_RULES['+'])
  rImp = RuleNode(RELATIONS_RULES['=>'])

  print("A + B => C")
  rAnd.connect(fA)
  rAnd.connect(fB)
  rImp.connect(rAnd)
  fC.connect(rImp)

  print("=AB")
  fA.activate(True)
  fB.activate(True)

  print("?C\n")
  fC.trigger()

  print("C:{}".format(bool(fC)))


def node_hard_test():
  fA = FactNode('A')
  fB = FactNode('B')
  fD = FactNode('D')
  fE = FactNode('E')
  fF = FactNode('F')
  fG = FactNode('G')
  fH = FactNode('H')
  fI = FactNode('I')
  fJ = FactNode('J')
  fK = FactNode('K')
  fL = FactNode('L')
  fM = FactNode('M')
  fN = FactNode('N')
  fO = FactNode('O')
  fP = FactNode('P')

  rImpBA = RuleNode(RELATIONS_RULES['=>'])
  rImpDEB = RuleNode(RELATIONS_RULES['=>'])
  rImpGHF = RuleNode(RELATIONS_RULES['=>'])
  rImpIJG = RuleNode(RELATIONS_RULES['=>'])
  rImpGH = RuleNode(RELATIONS_RULES['=>'])
  rImpLMK = RuleNode(RELATIONS_RULES['=>'])
  rImpOPL = RuleNode(RELATIONS_RULES['=>'])
  rImpOPN = RuleNode(RELATIONS_RULES['=>'])
  rImpNM = RuleNode(RELATIONS_RULES['=>'])

  rAndDE = RuleNode(RELATIONS_RULES['+'])
  rAndGH = RuleNode(RELATIONS_RULES['+'])
  rAndIJ = RuleNode(RELATIONS_RULES['+'])
  rAndLM = RuleNode(RELATIONS_RULES['+'])
  rAndOP = RuleNode(RELATIONS_RULES['+'])

  print("B     => A")
  print("D + E => B")
  print("G + H => F")
  print("I + J => G")
  print("G     => H")
  print("L + M => K")
  print("O + P => L + N")
  print("N     => M")
  rImpBA.connect(fB)
  fA.connect(rImpBA)

  rAndDE.connect(fD)
  rAndDE.connect(fE)
  rImpDEB.connect(rAndDE)
  fB.connect(rImpDEB)

  rAndGH.connect(fG)
  rAndGH.connect(fH)
  rImpGHF.connect(rAndGH)
  fF.connect(rImpGHF)

  rAndIJ.connect(fI)
  rAndIJ.connect(fJ)
  rImpIJG.connect(rAndIJ)
  fG.connect(rImpIJG)

  rImpGH.connect(fG)
  fH.connect(rImpGH)

  rAndLM.connect(fL)
  rAndLM.connect(fM)
  rImpLMK.connect(rAndLM)
  fK.connect(rImpLMK)

  rAndOP.connect(fO)
  rAndOP.connect(fP)
  rImpOPL.connect(rAndOP)
  rImpOPN.connect(rAndOP)
  fL.connect(rImpOPL)
  fN.connect(rImpOPN)

  rImpNM.connect(fN)
  fM.connect(rImpNM)

  print("=DEIJP")
  fD.activate(True)
  fE.activate(True)
  fI.activate(True)
  fJ.activate(True)
  fP.activate(True)

  print("?AFKP\n")
  fA.trigger()
  fF.trigger()
  fK.trigger()
  fP.trigger()

  print("A:{}".format(bool(fA)))
  print("F:{}".format(bool(fF)))
  print("K:{}".format(bool(fK)))
  print("P:{}".format(bool(fP)))
