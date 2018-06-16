# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    parser.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:30 by kcosta           #+#    #+#              #
#    Updated: 2018/06/16 12:58:07 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from expert_system.graph.fact_node import FactNode
from expert_system.graph.rule_node import RuleNode, RELATIONS_RULES

from expert_system.parser.lexer import Lexer
from expert_system.parser.token import Token, TOKEN_TYPE


class Parser:
  """Parser

  Parameters
  ----------
  filename: string
    Name of the file to be parse

  Attributes
  ----------
  _lexer  : object
    Lexer object for parsing the file
  _token  : object
    Current token read
  _nodes  : list of Node
    List of all Fact Node for tracking
  _queries: list of Node
    List of all Queries Node

  Exceptions:
  -----------
  OSError if could not open filename
  KeyError if unknown symbol met in file
  IndexError if mismatched parentheses
  """
  def __init__(self, filename):
    self._lexer = Lexer(filename)
    self._token = Token(TOKEN_TYPE['Newline'])
    self._nodes = []

  def parse(self):
    """Parse file and create all node connections

    Exceptions
    ----------
    KeyError if node not found
    """
    while self._token.type != TOKEN_TYPE['EOF']:
      self._token = self._lexer.lexer()

      if self._token.type == TOKEN_TYPE['Symbol']:
        if self._token == '=':
          self.parse_initial_facts()
        elif self._token == '?':
          self.parse_queries()
        elif self._token == '(' or self._token == ')':
          self.parse_fact()
        else:
          self._lexer.raise_KeyError()

      elif self._token.type == TOKEN_TYPE['Fact']:
        self.parse_fact()

  def create_nodes(self, postfix_exp):
    """Create nodes from postfix expression

    Parameters
    ----------
    postfix_exp: list of Token
      Postfix expression

    Exceptions
    ----------
    IndexError if mismatched number of arguments
    """

    stack = []
    for token in postfix_exp:

      if token.type == TOKEN_TYPE['Fact']:
        try:
          node = self.find_node(token)
        except:
          node = FactNode(token._value)
          self._nodes.append(node)

        if node not in stack:
          stack.append(node)

      elif token.type == TOKEN_TYPE['Symbol']:
        node = RuleNode(RELATIONS_RULES[token._value])

        if token == '=>':
          result = stack.pop()
          trigger = stack.pop()
          node.connect(trigger)
          result.connect(node)
          return

        elif token == '!':
          invert = stack.pop()
          node.connect(invert)

        else:
          lhs = stack.pop()
          rhs = stack.pop()
          node.connect(lhs)
          node.connect(rhs)
        stack.append(node)

  def parse_fact(self):
    """Parse all facts and create a postfix expression

    Exceptions
    ----------
    KeyError if node not found
    IndexError if mismatched parentheses
    """
    output_queue = []
    operator_stack = []

    while self._token.type != TOKEN_TYPE['Newline']:

      if self._token.type == TOKEN_TYPE['Fact']:
        output_queue.append(self._token.clone())

      elif self._token.type == TOKEN_TYPE['Symbol']:
        if self._token == '?' or self._token == '=' or self._token == '>':
          self._lexer.raise_KeyError()
        elif self._token == '(':
          operator_stack.append(self._token.clone())
        elif self._token == ')':
          while operator_stack[-1] != '(':
            output_queue.append(operator_stack.pop())
          operator_stack.pop()
        else:
          while (len(operator_stack) != 0 and
                  operator_stack[-1] != '(' and
                  RELATIONS_RULES[operator_stack[-1]._value] >=
                  RELATIONS_RULES[self._token._value]):
            output_queue.append(operator_stack.pop())
          operator_stack.append(self._token.clone())

      elif self._token.type == TOKEN_TYPE['EOF']:
        self._lexer.raise_KeyError()

      self._token = self._lexer.lexer()

    for op in reversed(operator_stack):
      if op == '(' or op == ')':
        raise IndexError('Mismatched parentheses')
      output_queue.append(op)

    self.create_nodes(output_queue)

  def parse_initial_facts(self):
    """Activate all initial facts nodes

    Exceptions
    ----------
    KeyError if node not found
    """
    # for node in self._nodes:
    #   node.reset()

    self._token = self._lexer.lexer()
    while self._token.type != TOKEN_TYPE['Newline']:

      if self._token.type == TOKEN_TYPE['Fact']:
        self.find_node(self._token).activate(True)

      elif self._token.type != TOKEN_TYPE['Whitespace']:
        if self._token.type != TOKEN_TYPE['Comment']:
          self._lexer.raise_KeyError()

      self._token = self._lexer.lexer()

  def parse_queries(self):
    """Parse all Queries node

    Exceptions
    ----------
    KeyError if node not found
    """
    self._token = self._lexer.lexer()
    self._queries = []

    while self._token.type != TOKEN_TYPE['Newline']:

      if self._token.type == TOKEN_TYPE['Fact']:
        self._queries.append(self.find_node(self._token))

      elif self._token.type == TOKEN_TYPE['EOF']:
        break

      elif self._token.type == TOKEN_TYPE['Symbol']:
        self._lexer.raise_KeyError()

      self._token = self._lexer.lexer()

  def evaluate_queries(self):
    for node in self._queries:
      node.evaluate()
      print("{}:{}".format(node.name, bool(node)))

  def find_node(self, name):
    """Return node based on it's name

    Exceptions
    ----------
    KeyError if node not found
    """
    for node in self._nodes:
      if node.name == name:
        return node
    self._lexer.raise_KeyError()
