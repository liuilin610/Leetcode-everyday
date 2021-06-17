# Time: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        A = []
        while head:
            A.append(head.val)
            head = head.next
        
        n = len(A)
        res, stack ＝ [0]* n, []
        
        for i in range(n):
            while stack and ( A[i] > A[stack[-1]] ):
                res[stack.pop() ] = A[i]
            stack.append(i)
        return res