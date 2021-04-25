# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

# I iteratively
(class Solution:
    def reverseList(self, head: ListNode) -> ListNode:)
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

# one line python 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev
    
# recursive
class Solution:
    def reverseList(self, head: ListNode, prev= None) -> ListNode:
        if not head: return None
        prev = None

        cur, head.next = head.next, prev
        return self.reverseList(cur, head)