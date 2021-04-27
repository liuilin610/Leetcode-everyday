# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(2log(n))
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)
        if (ldepth == rdepth):
            return pow( 2, ldepth) + self.countNodes(root.right)
        else:
            return pow( 2, rdepth) + self.countNodes(root.left)

    def depth(self, root):
        if not root: return 0
        return 1 + self.depth(root.left)

# Time complexity: O(n)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return ( 0 if not root else ( 1 + self.cuntNodes(roo.left) + self.countNodes(root.right)))