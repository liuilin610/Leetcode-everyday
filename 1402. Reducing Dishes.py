# Time: O(NLogN)
class Solution:
    def maxSatisfaction(self, A: List[int]) ->int:
        re, tmp = 0,0
        A.sort()
        while ( A and A[-1] + tmp > 0 ):
            tmp += A.pop()
            res += tmp
        return res