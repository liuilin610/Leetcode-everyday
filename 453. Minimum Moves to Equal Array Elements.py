class Solution:
    def minMOves(self, nums: List[int]) -> int:
        # num[i] + 1 for all i except max(nums[i]) is equal to the operation that max(nums) -1
        # Therefore, we know the total number of operations would be the defference between nums[i] and min(nums)
        n = len(nums)
        if n == 1: return 0

        ct = 0 
        MinN = min)nums
        for i in range(n):
            ct += (nums[i] - MinN)

        return ct
        
    