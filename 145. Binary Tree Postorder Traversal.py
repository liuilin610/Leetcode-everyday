# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root: TreeNode) -> List[int]:
        # III
        if not root: return []
        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            tmp = stack.pop()
            cur = tmp.left
        return res [::-1]
        """
        # II. dfs
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        res = []
        dfs(root)
        return res
        """
        '''
        # I
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]
        '''