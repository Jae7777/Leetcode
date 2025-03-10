# https://neetcode.io/problems/binary-tree-diameter
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def diameter(r):
            nonlocal res
            if not r: return 0
            l, r = diameter(r.left), diameter(r.right)
            res = max(res, l + r)
            return max(l , r) + 1
        diameter(root)
        return res
        