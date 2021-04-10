# Definition for a binary tree node.
#class TreeNode:
#   def __init__(self, val = 0, left = None, right = None):
#       self.val = val
#       self.left = left
#       self.right = right
class Solution:
    def recoverFromPreorder(self, S: str ) -> TreeNode:
        res = {-1: TreeNode(0) }
        def addtree(v, p):
            res[p] = TreeNode(int(v))
            if (not res[p - 1].left):
                res[p - 1].left = res[p]
            else:
                res[p - 1].right = res[p]
        # initial treeNode.val and depth
        val, dep = '', 0
        for c in S:
            if ( c != '-' ):
                val += c
            elif val:
                addTree(val, dep)
                val, dep = '', 1
            else:
                dep += 1
        addTree(val, dep)
        return res[0]