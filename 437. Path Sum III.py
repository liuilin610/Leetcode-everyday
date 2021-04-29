# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(root, sumlist):
            if not root: return 0
            sumlist = [root.val + num for num in sumlist] + [root.val]
            return sumlist.count(targetSum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return (root, [])