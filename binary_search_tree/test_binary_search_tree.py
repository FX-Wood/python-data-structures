import pytest
from BinarySearchTree import BinarySearchTree
from TreeNode import TreeNode

@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(10)
    tree.insert(1)
    return tree

class TestTree():
    def test_defined(self, tree):
        assert tree != None
    def test_left_defined(self, tree):
        assert tree.root.left != None
    def test_right_defined(self, tree):
        assert tree.root.right != None

    def test_in_order_traversal(self, tree):
        assert tree.traverse('in_order') == [1, 5, 10]

    def test_pre_order_traversal(self, tree):
        assert tree.traverse('pre_order') == [5, 1, 10]

    def test_post_order_traversal(self, tree):
        assert tree.traverse('post_order') == []