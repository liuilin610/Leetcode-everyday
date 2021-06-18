# Time: O(N)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        res, presum, dic = 0, 0, {}

        for i in range(n):
            presum = presum - 1 if ( hours[i] > 0 ) else presum + 1

            dic.setdefault(presum, i)
            # count presum < -1 from the index = 0
            if ( presum < 0 ):
                res = i + 1
            # the subarray with sum = -1
            if ( presum + 1 in dic ):
                res = max( res, i - dic[presum] )
        return res