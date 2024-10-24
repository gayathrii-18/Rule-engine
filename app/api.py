import re
from .models import Node, NodeType

def create_rule(rule_string):
    tokens = tokenize(rule_string)
    return parse_expression(tokens)

def tokenize(rule_string):
    return re.findall(r'\(|\)|\w+|[<>=]+|\d+|AND|OR|\'[^\']*\'', rule_string)

def parse_expression(tokens):
    if tokens[0] == '(':
        tokens.pop(0)  # Remove opening parenthesis
        left = parse_expression(tokens)
        if tokens[0] in ['AND', 'OR']:
            op = tokens.pop(0)
            right = parse_expression(tokens)
            tokens.pop(0)  # Remove closing parenthesis
            return Node(NodeType.OPERATOR, op, left, right)
        else:
            tokens.pop(0)  # Remove closing parenthesis
            return left
    else:
        attribute = tokens.pop(0)
        operator = tokens.pop(0)
        value = tokens.pop(0)
        return Node(NodeType.OPERAND, f"{attribute} {operator} {value}")

def combine_rules(rules):
    ast_rules = [create_rule(rule) for rule in rules]
    while len(ast_rules) > 1:
        left = ast_rules.pop(0)
        right = ast_rules.pop(0)
        combined = Node(NodeType.OPERATOR, "AND", left, right)
        ast_rules.insert(0, combined)
    return ast_rules[0]

def evaluate_rule(rule_json, data):
    def evaluate_node(node):
        if node["type"] == NodeType.OPERATOR.value:
            left_result = evaluate_node(node["left"])
            right_result = evaluate_node(node["right"])
            return left_result and right_result if node["value"] == "AND" else left_result or right_result
        else:
            attribute, operator, value = node["value"].split()
            actual_value = data.get(attribute)
            if operator == "=":
                return actual_value == value.strip("'")
            elif operator == ">":
                return float(actual_value) > float(value)
            elif operator == "<":
                return float(actual_value) < float(value)
    
    return evaluate_node(rule_json)
