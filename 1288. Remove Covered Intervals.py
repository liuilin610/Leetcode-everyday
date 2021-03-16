class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = intervals.sort(key = lambda u:(u[0], -u[1]))
        n = len(intervals)
        res , rmax = n, intervals[0][1]
        for i in range(1,n):
            if intervals[i][1] <= rmax:
                res -= 1
            else:
                rmax = intervals[i][1]
        return res