# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        setg = set(G)
        ct = 0

        while head:
            if (head.val in setg) and ( ( head.next and head.next.val not in setg) or ( not head.next)):
                ct += 1
            head = head.next
        return ct