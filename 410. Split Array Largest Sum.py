class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary Search 
        # Time Complexity : O( nlogn); Space: O (1)
        L, R = max(nums), sum(nums)

        # use mid to count the amount of subarrays to find the min (max(sum(subarray)))
        # ct : the number of subarray
        # SumSub : sum of subarray

        def TestMid(mid):
            ct = 1
            SumSub = 0
            for num in nums:
                if SumSub + num > mid:
                    SumSub = num
                    ct += 1
                else:
                    Sumsub += num
            return ct > m

        while ( L < R ):
            mid = ( L + R ) // 2
            SmallMid = TestMid(mid)
            if SmallMid:
                L = mid + 1
            else:
                R = mid
        return L