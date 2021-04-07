# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0: return None
        root = TreeNode(postorder[-1])
        Iroot = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: Iroot], postorder[: Iroot])
        root.right = self.buildTree(inorder[Iroot + 1:], postorder[Iroot:-1])
        return root