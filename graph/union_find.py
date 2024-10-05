from typing import Dict


A = [
    [0, 1, 4],
    [0, 2, 3],
    [1, 1, 2],
    [1, 3, 4],
    [1, 1, 4],
    [1, 3, 2],
    [0, 1, 3],
    [1, 2, 4],
    [1, 3, 0],
    [0, 0, 4],
    [1, 0, 2],
    [1, 3, 0],
]


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def find_set(node: Node):
    if node.parent is node:
        return node
    else:
        root = find_set(node.parent)
        node.parent = root
        return root


def unite(left: Node, right: Node):
    left_root = find_set(left)
    right_root = find_set(right)
    if left_root.rank == right_root.rank:
        left_root.parent = right_root
        right_root.rank += 1
    elif left_root.rank < right_root.rank:
        left_root.parent = right_root
    else:
        right_root.parent = left_root


def same(left: Node, right: Node):
    left_root = find_set(left)
    right_root = find_set(right)
    return left_root is right_root


node_list: Dict[int, Node] = {}


def get_node(id):
    if id in node_list:
        return node_list[id]

    node = Node(id)
    node_list[id] = node
    return node


for row in A:
    command = row[0]
    left = get_node(row[1])
    right = get_node(row[2])
    if command == 0:
        unite(left, right)
    elif command == 1:
        print(same(left, right))
