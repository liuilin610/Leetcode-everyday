class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1: return n

        dp = [1]*n
        if i in range(n):
            # only need to run the list[0-, i-1] + list[i]
            for j in range(i-1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(d[i], dp[j]+1)
                    break
        return n -max(dp)

        # run out of time with overlapping calculation 
        '''
        for i in range(n):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j]+1 )
        return n- max(dp)                
        '''