class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # preset key = 0 in dict and its value -1 for at least two elements sum!
        dict = {0: -1}
        n = len(nums)
        sumn = 0

        for i in range(nums):
            sumn = ( sumn + nums[i]) % k
            if ( sumn not in dict ):
                dict[sumn] = i
            elif ( i - dict[sumn] >= 2 ):
                return True
        return False