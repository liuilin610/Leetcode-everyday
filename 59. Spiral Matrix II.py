class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        List = [[0]*n for i in range(n)]
        ct = 1
        t, r, d, l = 0, n-1, n-1, 0
        while ct <= n*n:
            for i in range(l, r+1):
                List[t][i] = ct
                ct += 1
            t += 1
            for i in range(t, d+1):
                List[i][r] = ct
                ct += 1
            r -= 1
            for i in range(r, l-1, -1):
                List[d][i] = ct
                ct += 1
            d -= 1
            for i in range(d, t-1, -1):
                List[i][l] = ct
                ct += 1
            l += 1
        return List