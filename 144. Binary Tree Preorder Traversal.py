# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root: TreeNode) -> List[int]:
        # III
        if not root: return []
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            cur = tmp.right
        return res
               
        # II dfs
        def dfs(node):
            if not node:
                return []
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        res =[]
        dfs(root)
        return res
        """
        '''
        # I general
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
        '''