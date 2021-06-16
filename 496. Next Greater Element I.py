# Timee: O(N)
# maintain a non-increasing stack!
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic2, stack = {}, []
        n = len(nums2)

        for i in range(n):
            while stack and ( nums2[i] > stack[-1] ):
                dic2[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        return [ dic2.get(x, -1) for x in nums2 ]