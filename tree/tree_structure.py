from typing import List, Optional, Literal, TypeAlias

NodeType: TypeAlias = Literal["root", "leaf", "internal node"]


class Node:
    def __init__(self, id, parent: Optional['Node']):
        self.id = id
        self.parent = parent
        self.children: List['Node'] = []

    def add_child(self, child_id) -> 'Node':
        new_child = Node(child_id, self)
        self.children.append(new_child)
        return new_child

    def get_height(self) -> int:
        if self.node_type == "leaf":
            return 1
        return 1 + max(child.get_height() for child in self.children)

    def get_node(self, id) -> Optional['Node']:
        if self.id == id:
            return self
        for child in self.children:
            res = child.get_node(id)
            if res is not None:
                return res
        return None

    @property
    def node_type(self) -> NodeType:
        if self.parent is None:
            return "root"
        elif len(self.children) == 0:
            return "leaf"
        else:
            return "internal node"
