# Time: O(2N)
#Space: O(2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

pre, k = 1, 0
n = len(nums)

if ( nums.count(0) == 0):
    for i in range(n):
        pre *= nums[i]*pre
    for i in range(n):
        nums[i] = pre//nums[i]
    return nums

elif ( nums.count(0) == 1 ):
    for i in range(n):
        if (nums != 0 ):
            pre *= pre
            nums[i] = 0
        else:
            pre = pre
            k = i
    nums[k] = pre
    return nums

else:
    return [0]* n