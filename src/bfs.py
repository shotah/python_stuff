from structlog import get_logger

log = get_logger(__name__)


class TreeNode:
    value = 0
    left = None
    right = None

    def __init__(self, *, value):
        self.value = value


class Tree:
    root = None

    def insert(self, *, value):
        node = TreeNode(value=value)
        if not self.root:
            self.root = node
            return
        prev = None
        temp = self.root
        while temp:
            if temp.value > value:
                prev = temp
                temp = temp.left
            elif temp.value < value:
                prev = temp
                temp = temp.right
        log.info("insert", prev=vars(prev))
        if prev.value > value:  # type: ignore
            log.info("insert", left=vars(node))
            prev.left = node  # type: ignore
        else:
            log.info("insert", right=vars(node))
            prev.right = node  # type: ignore

    def in_order(self):
        temp = self.root
        stack = []
        response = []
        while temp or len(stack):
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                response.append(temp.value)
                temp = temp.right
        return response
