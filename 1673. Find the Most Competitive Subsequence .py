# Time: O(N)
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i, a in enumerate(nums):
            while res and ( res[-1] > a ) and ( len(res) + ( len(nums) - (i + 1)) <= k ):
                res.pop()
            if ( len(res) < k ):
                res.append(a)
        return res