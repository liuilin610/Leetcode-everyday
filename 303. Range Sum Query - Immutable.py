# Space: O(N)
# Time: O(1)
class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0]
        prefix = 0
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            self.presum.append(prefix)


    def sumRange(self, left: int, right: int) -> int:
        return ( self.presum(right+1) - self.presum(left) )