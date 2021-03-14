class Solution:
    def insert(self, A: List[List[int]], B: List[int]) -> List[List[int]]:
        n = len(A)
        # corner cases A = []; [B] < A ; A > [B]
        if n == 0: return [B]
        if B[1] <A[0][0] : return [B] +A
        if B[0] > A[-1][1]: return A + [B]
        res = []
        L, H = 0, -1

        for i in range(n):
            if (A[i][0] >= B[0]) or (A[i][1] >= B[0]):
                B[0] = min(B[0], A[i][0])
                L = i
                break
        
        for i in range(L, n):
            if (A[i][0] <= B[1]) and (A[i][0] <= B[1]):
                B[1] = max(B[1], A[i][1])
                H = i
                break
            if A[i][0] > B[1]:
                B[1] = max (B[1], A[i-1][1])
                H = i -1
                break
        if L > 0:
            res += A[: L]
        res.append([B])
        if H > -1 and H < n-1:
            res += A[H+1:]
        return res