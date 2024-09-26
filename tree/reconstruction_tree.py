class Node:
    def __init__(self, id, parent=None,  left=None, right=None):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def children_len(self):
        cnt = 0
        cnt += 1 if self.left else 0
        cnt += 1 if self.right else 0
        return cnt


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


def get_successor(x: Node):
    if x.right:
        return get_min(x)

    p = x.parent
    while p and x.id != p.left:
        x = p
        p = p.parent
    return p


def get_min(x: Node):
    while x.left:
        x = x.left
    return x


def delete(z: Node):
    y = None
    if z.left is None or z.right is None:
        y = z
    else:
        y = get_successor(z)

    if not y:
        # never happen
        return
    child = y.left if y.left else y.right

    if child:
        child.parent = y.parent

    if not y.parent:
        # y is root
        return
    elif y.id < y.parent.id:
        y.parent.left = child
    else:
        y.parent.right = child

    if y != z:
        z.id = y.id


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
