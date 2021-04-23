# similar as 315

# presum + hashmap
# O(n + (upper - lower + 1)*n)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for i in nums:
            presum.append(presum[-1] + i)

        record = collections.defaultdict(int)
        res = 0

        for psum in presum:
            for target in range(lower, upper + 1):
                if ( psum - target in record ):
                    res += record[psum - target]
            record[psum] += 1
        return res

# Time complexity: O(nlogn)
# presum + mergesort
class Solution: 
    def countRangeSum ( self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for i in nums:
            presum.append(presum[-1] + i )

        def mergesort(l, r):
            mid = (l + r) //2
            if ( l == mid ): return 0

            ct = mergesort(l, mid) + mergesort( mid, r)
            i = j = mid
            for left in presum[l: mid]:
                while ( i < r ) and ( presum[i] - left  < lower ):
                    i += 1
                while ( j < r ) and ( presum[j] - left <= upper ):
                    j += 1
                ct += j - i
            presum[l, r] = sorted ( presum[l, r])
            return ct
        return mergesort(0, len(presum))