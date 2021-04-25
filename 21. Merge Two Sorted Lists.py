# Definition for single_linked list.
# class ListNode:
#   def __init__( self, val = 0, next = None):
#       self.val = val
#       self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode ) -> ListNode:
        if ( not l1 ): return l2
        if ( not l2 ): return l1

        new_head = ListNode(0)
        move = new_head
        while ( l1 and l2 ):
            if ( l1.val > l2.val ):
                move.next = l2
                l2 = l2.next
            else:
                move.next = l1
                l1 = l1.next
            move = move.next
        move.next = l1 if l1 else l2
        return new_head.next