# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            cur, val, path = queue.pop(0)
            if ( not cur.left and not cur.right and val == Sum):
                res.append(path)
            if cur.left:
                queue.append(( cur.left, cur.left.val + val, path +[cur.left.val]))
            if cur.right:
                queue.append( ( cur.right, cur.right.val + val, path + [cur.right.val]))
        return res
#DFS
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        res = []
        self.dfs(root, target, [], res)
        return res

    def dfs(self, root, Sum, path, res):
        if root:
            if ( not root.left and root.right and root.val == Sum):
                path.append(root.val)
                res.append(path)
            Sum -= root.val
            self.dfs(root.left, Sum, path, res)
            self.dfs(root.right, Sum, path, res)


