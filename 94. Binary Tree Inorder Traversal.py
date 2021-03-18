# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: TreeNode) -> List[int]:
        #III
        if not root: return []
        res, stack = [],[]
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            res.append(tmp.val)
            cur = tmp.right
        return res

        """
        # II. dfs
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        res = []
        dfs(root)
        return res
        """
        '''
        # I. general
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        '''

        
