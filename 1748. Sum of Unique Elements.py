class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0
        for c in nset:
            if nums.count(c) == 1:
                res += c
        return res
