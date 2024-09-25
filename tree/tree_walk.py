from typing import Union


class Node:
    def __init__(self, id, left_id, right_id):
        self.id = id
        left = Node(left_id, -1, -1) if left_id != -1 else None
        right = Node(right_id, -1, -1) if right_id != -1 else None
        self.left = left
        self.right = right

    def get_node(self, id) -> Union['Node', None]:
        if self.id == id:
            return self
        return (self.left and self.left.get_node(id)) or (self.right and self.right.get_node(id))

    def preorder_tree_walk(self, A):
        A.append(self.id)
        if self.left and self.left.id != -1:
            self.left.preorder_tree_walk(A)
        if self.right and self.right.id != -1:
            self.right.preorder_tree_walk(A)

    def in_order_tree_walk(self, A):
        if not self.left or self.left.id == -1:
            A.append(self.id)
            return
        else:
            self.left.in_order_tree_walk(A)
            A.append(self.id)

        if self.right and self.right.id != -1:
            self.right.in_order_tree_walk(A)

    def postorder_tree_walk(self, A):
        if not self.left or self.left.id == -1:
            A.append(self.id)
            return
        else:
            self.left.postorder_tree_walk(A)
        if self.right and self.right.id != -1:
            self.right.postorder_tree_walk(A)
        A.append(self.id)


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root

    def add_node(self, id, left_id, right_id):
        node = self.root.get_node(id)
        if not node:
            node = Node(id, left_id, right_id)
            return node

        left = Node(left_id, -1, -1)
        right = Node(right_id, -1, -1)
        node.left = left
        node.right = right
        return node

    def preorder_tree_walk(self):
        A = []
        self.root.preorder_tree_walk(A)
        print(*A)

    def in_order_tree_walk(self):
        A = []
        self.root.in_order_tree_walk(A)
        print(*A)

    def postorder_tree_walk(self):
        A = []
        self.root.postorder_tree_walk(A)
        print(*A)


root = Node(0, 1, 4)
bt = BinaryTree(root)
bt.add_node(1, 2, 3)
bt.add_node(2, -1, -1)
bt.add_node(3, -1, -1)
bt.add_node(4, 5, 8)
bt.add_node(5, 6, 7)
bt.add_node(6, -1, -1)
bt.add_node(7, -1, -1)
bt.add_node(8, -1, -1)

bt.preorder_tree_walk()
bt.in_order_tree_walk()
bt.postorder_tree_walk()
