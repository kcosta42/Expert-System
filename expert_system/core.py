# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    core.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:22:03 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 22:10:59 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.parser.parser import Parser


def parse_file(filename, quiet):
  try:
    parser = Parser(filename)
    if not quiet:
      Parser.Verbose = True
    parser.parse()
  except OSError as e:
    print("\n{error}".format(error=e))
  except KeyError as e:
    print("\n{error}".format(error=e))
  except IndexError as e:
    if str(e) == "pop from empty list":
      print("\nError in expression")
    else:
      print("\n{error}".format(error=e))
  except Exception:
    print("\nError while parsing file")
