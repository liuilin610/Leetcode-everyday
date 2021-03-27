class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        if (nums[0] > target): return 0
        if (nums[-1] <= target/2 ): return 2 ** (n) -1

        res = 0
        Indexf, Indexi = n-1, 0
        while (Indexf >= Indexi):
            if (nums[Indexi] + nums[Indexf] <= target):
                res += 2 ** (Indexf - Indexi)
                Indexi += 1
            else:
                Indexf -= 1
        return res % (10 ** 9 + 7)
