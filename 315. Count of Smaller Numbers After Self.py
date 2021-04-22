class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for n in reverse(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx, n)
        return res[::-1]

# Binary indexed tree
class Solution:
    def countSmaller(self, nums: List[Lis[int]]) -> List[int]:
        rank = {val: i + 1 for i, val in enumerate(sorted( nums))}
        n, res = len(nums), []
        BITree = [0] * ( n + 1)

        def update(i):
            while ( i <= n ):
                BITree += 1
                i += i & -i
            
        def presum(i):
            index = 0
            while i:
                index += BITree[i]
                i -= i & -i
            return index

        for i in reversed(nums):
            res.append( presum(rank[i]) - 1 )
            update( rank[i] )
        return res[::-1]

#Binary Indexed Tree
# lowbit
# C- index of binary indexed tree
# A- index of each elements
# C1 = A1
# C2 = A1 + A2
# C3 = A3
# C4 = A1 + A2 + A3 + A4
# C5 = A5
# C6 = A5 + A6
# C7 = A7
# C8 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
# lowbit(x) = x & -x ( or lowbit(x) = x & (~x + 1 )