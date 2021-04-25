# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int ) -> ListNode:
        if not head: return None
        res = p = ListNode(0)
        while head:
            if ( head.val != val ):
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        return res.next
        
# two pointer
class Solution:
    def removeElements(self, head: ListNode, val: int ) -> ListNode:
        if not head: return
        new_head = ListNode(0)
        new_head.next = head
        slow, fast = new_head, head
        while fast:
            if ( fast.val != val ):
                slow.next.val = fast.val
                slow = slow.next
            fast.next = fast
        slow.next = None
        return new_head.next

