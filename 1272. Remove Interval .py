class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        if toBeRemoved[0]> intervals[-1][1] or toBeRemoved[1] < intervals[0][0] : return intervals
        
        n = len(intervals)
        L, H = 0, -1
        res =[]
        for i in range(n):
            if intervals[i][0] <= toBeRemoved[0] and toBeRemoved[0] <= intervals[i][1]:
                intervals[i][1] = min(toBeRemoved[0], intervals[i][1])
                L = i
                break
        for j in range(L,n):
            if intervals[j][0] <= toBeRemoved[1] and toBeRemoved[1] <= intervals[j][1]:
                intervals[j][0] = max(intervals[j][0], intervals[1])
                H = j
                break
            if intervals[j][0] > toBeRemoved[1]:
                H = i-1
                break
        if L > 0: 
            res += intervals[:L]
            res.append(intervals[L])
        if L == H and H < n-1:
            res += intervals[H+1:]
        if H > L and H < n-1:
            res += intervals[H:]
        else: res = intervals
        return res
