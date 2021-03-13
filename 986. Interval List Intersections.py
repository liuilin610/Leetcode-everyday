class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(A), len(B)
        if n1 == 0 or n2 == 0: return []
        i,j = 0,0
        res = []

        while i< n1 and j < n2:
            L = max(A[i][0], B[j][0])
            H = min(A[i][1], B[j][1])
            if L <= H:
                res += [[L, H]]
            if A[i][1]< B[i][1]:
                i += 1
            else:
                j += 1
        return res