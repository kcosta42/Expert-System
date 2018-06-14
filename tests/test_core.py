# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_core.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 22:08:43 by kcosta           #+#    #+#              #
#    Updated: 2018/06/13 22:44:26 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.parser.scanner import Scanner


def scanner_test():
  scan = Scanner('README.md')
  byte = scan.read()
  while byte:
    print("%c" % int(byte), end="")
    byte = scan.read()