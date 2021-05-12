#Time: O(NlogN), Space: O(N)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = []
        A = sorted(nums)
        for i in range(len(nums)):
            if ( A[i] != nums[i]): res.append(i)
        return 0 if ( res == []) else ( res[-1] - res[0] + 1)

#Time: O(N); Space: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if ( n < 2 ): return 0

        pre1, pre2 = nums[0], nums[-1]
        final, ini = 0, n-1
        for i in range(n):
            # find the largest worng index for sorted array
            if ( nums[i] < pre1 ): final = i
            else: pre1 = nums[i]

            # find the smallest wrong index one
            if ( nums[n-1-i] > pre2 ): ini = n-1-i
            else: pre2 = nums[n-1-i]
        
        return 0 if ( final == 0) else ( final - ini + 1)