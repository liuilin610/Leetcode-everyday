# Time: O(N); Space: O(N)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        stack, res, ji = [], 0, -1

        for i in range( len(nums) ):
            if ( nums[i] < 0 ):
                stack.append(i)
            elif (nums[i] == 0 ):
                stack, ji = [], i
            if ( len(stack) % 2 == 0 ):
                res = max(res, i - ji )
            else:
                res = max(res, i - stack[0] )
        return res