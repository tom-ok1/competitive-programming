A = [1, 3, 4, 5, 10, 13, 14, 16, 19, 21]


class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right


def preorder(node: Node):
    print(node.id)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


def make_tree(left, right):
    if right < left:
        return None

    mid = (left + right) // 2
    left_node = make_tree(left, mid-1)
    right_node = make_tree(mid+1, right)
    return Node(A[mid], left_node, right_node)


def find(node, x1, x2):
    x = node.id
    if x1 <= x and x <= x2:
        print(x)
    if node.left and x1 <= x:
        find(node.left, x1, x2)
    if node.right and x <= x2:
        find(node.right, x1, x2)


points = [(1, 1), (3, 3), (4, 2), (5, 5), (10, 10),
          (13, 13), (14, 14), (16, 16), (19, 19), (21, 21)]


class DNode:
    def __init__(self, point: tuple[int, int], left, right):
        self.point = point
        self.left = left
        self.right = right


def make_nD_tree(points, depth=0):
    if len(points) == 0:
        return None

    axis = depth % 2
    points.sort(key=lambda point: point[axis])
    mid = len(points) // 2
    return DNode(
        point=points[mid],
        left=make_nD_tree(points[:mid], depth+1),
        right=make_nD_tree(points[mid+1:], depth+1)
    )


def find_nD(node, p1: tuple[int, int], p2: tuple[int, int], depth=0):
    x1, y1 = p1
    x2, y2 = p2
    x, y = node.point
    if x1 <= x and x <= x2 and y1 <= y and y <= y2:
        print(x, y)
    axis = depth % 2
    if axis == 0:
        if node.left and x1 <= x:
            find_nD(node.left, p1, p2, depth+1)
        if node.right and x <= x2:
            find_nD(node.right, p1, p2, depth+1)
    else:
        if node.left and y1 <= y:
            find_nD(node.left, p1, p2, depth+1)
        if node.right and y <= y2:
            find_nD(node.right, p1, p2, depth+1)


node = make_nD_tree(points)
find_nD(node, (2, 3), (16, 18))
