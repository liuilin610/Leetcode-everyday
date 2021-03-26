# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deletDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val: cur.next = cur.next.next
            else: cur = cur.next
        return head
        '''
        if not head or not head.next: return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
        '''
        '''
        if head is None or head.next is None: return head
        cur, next = head, head.next
        while cur and next:
            if cur.val != next.val: cur = cur.next
            else: cur.next = next.next
            next = next.next
        return head
        '''