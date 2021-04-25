# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverse(head):
            prev = ListNode(0)
            while head:
                head.next, prev, head = prev, head, head.next
            return prev

        res = head = ListNode(0)
        l1, l2 = reverse(l1), reverse(l2)
        carry = 0
        while ( l1 or l2 or carry != 0):
            v1 = v2 = 0
            if l1:
                v1, l1 = l1.val, l1.next
            if l2:
                v2, l2 = l2.val, l2.next
            carry, val = divmod( v1 + v2 + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return reverse(res.next)
