class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #dp
        n = len(points)
        if n <2: return n
        points.sort(key = lambda u:(u[0]))
        for i in range(n):
            for j in range(i-1, -1, -1):
                points[i][0] > points[j][1]:
                dp[i]= max(dp[i], dp[j]+1 )
        return max(dp)
        # two pointers
        '''
        n = len(points)
        H, L = points[0][1], points[0][0]
        res = 1
        for i in range(1, n):
            L = max(L, points[i][0])
            H = min(H, points[i][1])
            if H < L:
                res += 1
                L , H = points[i][0], points[i][1]
        return res
        '''