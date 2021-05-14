class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0] * (n+1) for i in range(m+1)]
        for i in range(1, 1+m):
            for j in range(1, 1+n):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] + matrix[i-1][j-1] -self.sum[i-1][j-1]     
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r2, c2 = r2+1, c2+1
return self.sum[r2][c2] -self.sum[r1][c2]-self.sum[r2][c1] + self.sum[r1][c1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               