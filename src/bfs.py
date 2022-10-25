from typing import Union

from structlog import get_logger

log = get_logger(__name__)


class TreeNode:
    value = 0
    left = None
    right = None

    def __init__(self, *, value: int):
        self.value = value
        self.left: Union[TreeNode, None] = None
        self.right: Union[TreeNode, None] = None


class Tree:
    def __init__(self, *, value: int):
        self.root: Union[TreeNode, None] = TreeNode(value=value)

    def __get_prev_node(self, *, root_node: Union[TreeNode, None], value: int):
        prev_node: Union[TreeNode, None] = None
        curr_node = root_node
        while curr_node:
            if curr_node.value > value:
                prev_node: Union[TreeNode, None] = curr_node
                curr_node: Union[TreeNode, None] = curr_node.left
            else:
                prev_node: Union[TreeNode, None] = curr_node
                curr_node: Union[TreeNode, None] = curr_node.right
        return prev_node

    def __set_prev_node(self, *, prev_node: Union[TreeNode, None], value: int):
        if prev_node:
            if prev_node.value > value:
                prev_node.left = TreeNode(value=value)
            else:
                prev_node.right = TreeNode(value=value)

    def insert(self, *, value: int):
        prev_node = self.__get_prev_node(root_node=self.root, value=value)
        self.__set_prev_node(prev_node=prev_node, value=value)

    def in_order(self):
        stack = []
        response = []
        while self.root or len(stack):
            if self.root:
                stack.append(self.root)
                self.root: Union[TreeNode, None] = self.root.left
            else:
                self.root = stack.pop()
                if self.root:
                    response.append(self.root.value)
                    self.root: Union[TreeNode, None] = self.root.right
        return response
