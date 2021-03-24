class Solution:
    def 132 patterm(self, nums: List[int]) -> bool:
        # store the maximum in stack and keep second larger value as k 
        # start from right end to get the maximum to garantee the second larger number at the right side
        # reture True if we could get the smaller value at the left side
        # time complexity: O(n); space complexity: O(2)

        n = len(nums)
        if n < 3: return False
        TmpStack = []
        k = - (10 ** 9 + 7)

        for i in range(n-1, -1, -1):
            if nums[i] < k:
                return True
            while TmpStack and (TmpStack[-1] < nums[i]):
                k = max(k, TmpStack.pop())
            TmpStack.append(nums[i])
        return False