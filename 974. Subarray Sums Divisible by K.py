class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #Here we consider the mode of K; k possible outcome
        # prefix : presum of nums
        res = prefix = 0
        count = [1] + [0] * ( k - 1 )
        for i in nums:
            prefix = ( prefix + i ) % k
            res += count[prefix]
            count[prefix] += 1
        return res
