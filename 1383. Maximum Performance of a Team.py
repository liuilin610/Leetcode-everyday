# Time: O(nlogn); Space: O(n)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        res = ssum = 0
        for e, s in sorted(zip(efficiency, speed), reverse = 1):
            heapq.heappush(h, s)
            ssum += s
            if ( len(h) > k):
                ssum -= heapq.heappop(h)
            res = max( res, e*ssum)
        return res
