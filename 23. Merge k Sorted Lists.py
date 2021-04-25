# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# divide and conquer
#Time complexity: O ( n log k)
class Solution:
    def mergeKLists(self,lists):
        if ( not lists ): return None
        if ( len(lists) == 1 ): return lists[0]
        mid = ( len(lists) // 2 )
        l, r = self.mergeKLists(lists[: mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = p = ListNode()

        while ( l and r ):
            if (l.val < r.val):
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next

class Solution:
    def mergeKLists(self,lists):
        heap = []
        for node in lists:
            heap.append( (node.val, node) )
        heapq.heapify(heap)
        head = ListNode(0)
        move = head
        while heap:
            pop = heapq.heapop(heap)
            move.next = ListNode( pop[0] )
            move = move.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next