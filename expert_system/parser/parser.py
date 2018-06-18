# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    parser.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:30 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 22:02:11 by kcosta          ###   ########.fr        #
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
  _rules  : list of list of Token
    List of all parsed rules in Reverse Polish notation

  Static Attributes
  -----------------
  Verbose: boolean
    Print log if True

  Exceptions:
  -----------
  OSError if could not open filename
  KeyError if unknown symbol met in file
  IndexError if mismatched parentheses
  """
  Verbose = False

  def __init__(self, filename):
    self._lexer = Lexer(filename)
    self._token = Token(TOKEN_TYPE['Newline'])
    self._nodes = []
    self._queries = []
    self._rules = []

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
        elif self._token == '(' or self._token == ')' or self._token == '!':
          self.parse_fact()
        else:
          self._lexer.raise_KeyError()

      elif self._token.type == TOKEN_TYPE['Fact']:
        self.parse_fact()

  def check_conflict(self, postfix_exp):
    for rules in self._rules:

      j = 0
      diff = False
      hasNotToken = False
      for i in range(0, len(rules)):
        while postfix_exp[j] == '!' and postfix_exp[j]._result:
          hasNotToken = True
          j += 1
          if (j >= len(postfix_exp)):
            break
        if postfix_exp[j] != rules[i]:
          diff = True
          break
        j += 1
        if (j >= len(postfix_exp)):
          break
      if not diff and hasNotToken:
        raise KeyError('Conflicting rules detected')
      elif not diff:
        return 1

    self._rules.append(postfix_exp[0:])
    return 0

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
    if self.check_conflict(postfix_exp):
      return

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

        if token == '=>' or token == '<=>':
          result = stack.pop()
          trigger = stack.pop()
          node.connect(trigger)
          result.connect(node)
          return

        elif token == '!':
          invert = stack.pop()
          if token._result:
            invert.connect(node)
          else:
            node.connect(invert)

        else:
          lhs = stack.pop()
          rhs = stack.pop()
          if token._result:
            lhs.connect(node)
            rhs.connect(node)
          else:
            node.connect(lhs)
            node.connect(rhs)
        stack.append(node)

  def parse_biconditional_fact(self, rev_exp):
    """Parse all biconditional fact from expression

    Parameters
    ----------
    rev_exp: List of Token
      Expression reversed

    Exceptions
    ----------
    KeyError if node not found
    IndexError if mismatched parentheses
    """
    output_queue = []
    operator_stack = []
    parsing_result = False

    for token in rev_exp:
      token._result = parsing_result

      if token.type == TOKEN_TYPE['Fact']:
        output_queue.append(token)

      elif token.type == TOKEN_TYPE['Symbol']:
        if token == '?' or token == '=' or token == '>' or token == '=>':
          self._lexer.raise_KeyError()

        elif token == '(':
          operator_stack.append(token)

        elif token == ')':
          while operator_stack[-1] != '(':
            output_queue.append(operator_stack.pop())
          operator_stack.pop()

        else:
          if token == '<=>':
            if not parsing_result:
              parsing_result = True
            else:
              self._lexer.raise_KeyError()

          while (len(operator_stack) != 0 and
                  operator_stack[-1] != '(' and
                  RELATIONS_RULES[operator_stack[-1]._value] >  # >=
                  RELATIONS_RULES[token._value]):
            output_queue.append(operator_stack.pop())
          operator_stack.append(token)

    for op in reversed(operator_stack):
      if op == '(' or op == ')':
        raise IndexError('Mismatched parentheses')
      output_queue.append(op)

    self.create_nodes(output_queue)


  def parse_fact(self):
    """Parse all facts and create a postfix expression

    Exceptions
    ----------
    KeyError if node not found
    IndexError if mismatched parentheses
    """
    expression = []
    output_queue = []
    operator_stack = []
    parsing_result = False
    is_biconditional = False

    while self._token.type != TOKEN_TYPE['Newline']:

      if self._token.type == TOKEN_TYPE['Fact']:
        print(self._token, end=" ") if Parser.Verbose else None
        expression.append(self._token.clone())
        output_queue.append(self._token.clone())

      elif self._token.type == TOKEN_TYPE['Symbol']:
        print(self._token, end=" ") if Parser.Verbose else None
        expression.append(self._token.clone())
        if self._token == '?' or self._token == '=' or self._token == '>':
          self._lexer.raise_KeyError()

        elif self._token == '(':
          operator_stack.append(self._token.clone())

        elif self._token == ')':
          while operator_stack[-1] != '(':
            output_queue.append(operator_stack.pop())
          operator_stack.pop()

        else:
          if self._token == '=>' or self._token == '<=>':
            if not parsing_result:
              is_biconditional = self._token == '<=>'
              parsing_result = True
            else:
              self._lexer.raise_KeyError()

          while (len(operator_stack) != 0 and
                  operator_stack[-1] != '(' and
                  RELATIONS_RULES[operator_stack[-1]._value] >  # >=
                  RELATIONS_RULES[self._token._value]):
            output_queue.append(operator_stack.pop())
          operator_stack.append(self._token.clone())

      elif self._token.type == TOKEN_TYPE['EOF']:
        self._lexer.raise_KeyError()

      self._token = self._lexer.lexer()
      self._token._result = parsing_result

    for op in reversed(operator_stack):
      if op == '(' or op == ')':
        raise IndexError('Mismatched parentheses')
      output_queue.append(op)

    print() if Parser.Verbose else None
    self.create_nodes(output_queue)

    if is_biconditional:
      self.parse_biconditional_fact(expression[::-1])

  def parse_initial_facts(self):
    """Activate all initial facts nodes

    Exceptions
    ----------
    KeyError if node not found
    """
    print("\n=", end="") if Parser.Verbose else None

    for node in self._nodes:
      node.reset([])

    self._token = self._lexer.lexer()
    while self._token.type != TOKEN_TYPE['Newline']:

      if self._token.type == TOKEN_TYPE['Fact']:
        print(self._token, end="") if Parser.Verbose else None
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

    print("\n?", end="") if Parser.Verbose else None

    while self._token.type != TOKEN_TYPE['Newline']:

      if self._token.type == TOKEN_TYPE['Fact']:
        print(self._token, end="") if Parser.Verbose else None
        self._queries.append(self.find_node(self._token))

      elif self._token.type == TOKEN_TYPE['EOF']:
        break

      elif self._token.type == TOKEN_TYPE['Symbol']:
        self._lexer.raise_KeyError()

      self._token = self._lexer.lexer()

    self.evaluate_queries()

  def evaluate_queries(self):
    """Evaluate Queries"""
    print() if Parser.Verbose else None

    for node in self._nodes:
      node.evaluate([])

    for node in self._queries:
      node.evaluate([])
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
