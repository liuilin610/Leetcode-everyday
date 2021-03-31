class Solution:
    def Clumsy(self, N: int):
        if ( N <= 2): return 
        A, B = N // 4, N % 4
        res = 2 * (N * (N - 1) // (N - 2) )
        for i in range(A, 0, -1):
            K = 4 * i + B
            res = res - (K * ( K - 1 ) // ( K - 2 )) + ( K - 3 )
        
        if (B <= 2): res -= B
        if (B == 3): res -= 6
        return res