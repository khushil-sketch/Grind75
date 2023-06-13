""" INVERT BINARY TREE """

from typing import Any, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)


    def invert(root: Optional[TreeNode]):
        if root is None:
            return None

        elif root.left is None and root.right is None:
            return root

        else:
            new_right_subtree = invert(root.left)
            new_left_subtree = invert(root.right)
            inverted_tree = TreeNode(root.val, new_left_subtree, new_right_subtree)
            return inverted_tree

