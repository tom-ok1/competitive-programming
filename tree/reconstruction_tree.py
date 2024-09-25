class Node:
    def __init__(self, id, parent=None,  left=None, right=None):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right


def insert(root: Node, node: Node):
    p = None
    x = root
    while x:
        p = x
        if node.id < p.id:
            x = x.left
        else:
            x = x.right

    node.parent = p
    if not p:
        return
    if node.id < p.id:
        p.left = node
    else:
        p.right = node


def preorder(n: Node, A):
    A.append(n.id)
    if n.left:
        preorder(n.left, A)
    if n.right:
        preorder(n.right, A)


def inorder(n: Node, A):
    if n.left:
        inorder(n.left, A)
    A.append(n.id)
    if n.right:
        inorder(n.right, A)


root = Node(30)
insert(root, Node(88))
insert(root, Node(12))
insert(root, Node(1))
insert(root, Node(20))
insert(root, Node(17))
insert(root, Node(25))

A_p = []
A_i = []
preorder(root, A_p)
inorder(root, A_i)
print(*A_p)
print(*A_i)
