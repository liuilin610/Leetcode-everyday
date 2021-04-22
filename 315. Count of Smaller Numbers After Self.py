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


#Binay Indexed tree
class BIT(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i):
        while ( i < len(self.sums) ):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while ( i > 0 ):
            r += self.sums[i]
            i -= i & -i
        return r

class Solution(object):
    def coutSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(nums))}
        tree, res = BIT(len(hashTable)), []

        for i in range(len(nums)-1, -1, -1):
            res.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i] + 1])
        reurn res[::-1]

# mergesort
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range( len(enum))[::-1]:
                    if (not left or right ) and ( left[-1][1] > right[-1][1] ):
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller