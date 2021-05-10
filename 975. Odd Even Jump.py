#lee215
#Time : O(NlongN), Space: (O(N))
class Solution:
    def oddEvenJumps(self, arr: List[int] ) -> int:
        n = len(arr)
        next_h, next_l = [0] * n, [0] * n

        #sorted to get the position(index) of next higher number
        stack = []
        for a,i in sorted([a,i] for i, a in enumerate(arr)):
            while stack and (stack[-1] < i ):
                next_h[stack.pop()] = i
            stack.append(i)

        # use sorted( negative element to get the inverse sorted) arry to get the index of next lower
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and ( stack[-1] < i ):
                next_l[stack.pop()] = i
            stack.append(i)

        higher, lower = [0]* n, [0] * n
        #the lastest index could always arrive.
        higher[-1], lower[-1] = 1, 1
        for i in range(n-2, -1, -1):
            higher[i] = lower[next_h[i]]
            lower[i] = higher[next_l[i]]
        return sum(higher)

        