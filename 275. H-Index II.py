#Time complexity: O(N); Space:O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(n):
            # max h : n if the smallest citations > n, h-index = n
            if citations[i] >= n-i: return n-i
        return 0 # if no citations 