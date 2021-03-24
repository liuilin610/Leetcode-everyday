# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesII(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        dummy.next = head

        slow, fast = None, dummy

        while fast:
            slow = fast
            fast = fast.next
            while fast and fast.next and fast.val == fast.next.val:
                repeatedN = fast.val
                while fast and fast.val == repeatedN:
                    fast = fast.next
                slow.next = fast 
        return dummy.next