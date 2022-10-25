from __future__ import annotations

from structlog import get_logger

from ..src.bfs import Tree

log = get_logger(__name__)


def test_tree_root():
    test_tree = Tree()
    test_tree.insert(value=30)
    log.info("test_tree", test_tree=vars(test_tree.root))
    assert test_tree.root.value == 30  # type: ignore


def test_tree_left_right():
    test_tree = Tree()
    test_tree.insert(value=30)
    test_tree.insert(value=50)
    test_tree.insert(value=15)
    log.info("test_tree", test_tree=vars(test_tree.root))
    assert test_tree.root.left.value == 15  # type: ignore
    assert test_tree.root.right.value == 50  # type: ignore


def test_tree_grandchild_left():
    test_tree = Tree()
    test_tree.insert(value=30)
    test_tree.insert(value=50)
    test_tree.insert(value=15)

    test_tree.insert(value=20)
    test_tree.insert(value=10)
    log.info("test_tree", test_tree=vars(test_tree.root))
    assert test_tree.root.left.left.value == 10  # type: ignore
    assert test_tree.root.left.right.value == 20  # type: ignore


def test_tree_grandchild_right():
    test_tree = Tree()
    test_tree.insert(value=30)
    test_tree.insert(value=50)
    test_tree.insert(value=15)

    test_tree.insert(value=20)
    test_tree.insert(value=10)

    test_tree.insert(value=40)
    test_tree.insert(value=60)
    log.info("test_tree", test_tree=vars(test_tree.root))
    assert test_tree.root.right.left.value == 40  # type: ignore
    assert test_tree.root.right.right.value == 60  # type: ignore


def test_tree_in_order():
    test_tree = Tree()
    test_tree.insert(value=30)
    test_tree.insert(value=50)
    test_tree.insert(value=15)

    test_tree.insert(value=20)
    test_tree.insert(value=10)

    test_tree.insert(value=40)
    test_tree.insert(value=60)
    log.info("test_tree", test_tree=vars(test_tree.root))
    assert test_tree.in_order() == [10, 15, 20, 30, 40, 50, 60]
