class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.res, self.ind = [], 0

        def dfs(node):
            if ( not node or self.ind == len(voyage)):  return
            if ( node.val != voyage[self.ind]):
                self.res.append(None)
                return
            dr, self.ind = 1, self.ind
            if ( node.left and node.left.val != voyage[self.ind]):
                self.res.append(node.val)
                dr = -1
            
            for child in [node.left, node.right][:: dr]:
                dfs(child)
        dfs(root)
        return ([-1] if None in self.res else self.res)