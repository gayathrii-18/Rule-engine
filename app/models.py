from enum import Enum

class NodeType(Enum):
    OPERATOR = "operator"
    OPERAND = "operand"

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            "type": self.type.value,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

    @classmethod
    def from_dict(cls, data):
        node = cls(NodeType(data["type"]), data["value"])
        if data["left"]:
            node.left = cls.from_dict(data["left"])
        if data["right"]:
            node.right = cls.from_dict(data["right"])
        return node
