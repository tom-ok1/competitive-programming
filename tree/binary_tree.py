from typing import Optional, TypeAlias, Literal, Dict

NodeType: TypeAlias = Literal["root", "leaf", "internal node"]


class Node:
    """
    二分木のノードを表すクラス。
    """

    def __init__(self, node_id: int):
        self.id: int = node_id
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.parent: Optional['Node'] = None
        self.depth: int = 0
        self.height: int = 0
        self.sibling: Optional['Node'] = None

    @property
    def node_type(self) -> NodeType:
        if self.parent is None:
            return "root"
        elif self.left is None and self.right is None:
            return "leaf"
        else:
            return "internal node"

    def update_height(self) -> int:
        """
        ノードの高さを更新し、返します。
        """
        left_height = self.left.update_height() if self.left else 0
        right_height = self.right.update_height() if self.right else 0
        self.height = 1 + max(left_height, right_height)
        return self.height

    def __repr__(self):
        return f"Node(id={self.id})"


class BinaryTree:
    """
    二分木を表すクラス。
    """

    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.root: Optional[Node] = None

    def add(self, node_id: int, left_id: Optional[int], right_id: Optional[int]):
        """
        ノードをツリーに追加します。
        """
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)
        node = self.nodes[node_id]

        if self.root is None:
            self.root = node
            node.depth = 0
        elif node.parent is None and node != self.root:
            raise ValueError(f"Node {node_id} has no parent but is not root.")

        # 左の子ノードを追加
        if left_id is not None and left_id != -1:
            if left_id not in self.nodes:
                self.nodes[left_id] = Node(left_id)
            left_node = self.nodes[left_id]
            node.left = left_node
            left_node.parent = node
            left_node.depth = node.depth + 1
            left_node.sibling = node.right
        else:
            node.left = None

        # 右の子ノードを追加
        if right_id is not None and right_id != -1:
            if right_id not in self.nodes:
                self.nodes[right_id] = Node(right_id)
            right_node = self.nodes[right_id]
            node.right = right_node
            right_node.parent = node
            right_node.depth = node.depth + 1
            right_node.sibling = node.left
        else:
            node.right = None

        # 兄弟ノードの設定
        if node.left and node.right:
            node.left.sibling = node.right
            node.right.sibling = node.left

    def update_heights(self):
        """
        すべてのノードの高さを更新します。
        """
        if self.root:
            self.root.update_height()
