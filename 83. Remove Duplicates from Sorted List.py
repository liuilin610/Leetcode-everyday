# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deletDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur, next = head, head.next
        while cur and next:
            if cur.val != next.val: cur = cur.next
            else: cur.next = next.next
            next = next.next
        return head