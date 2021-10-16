# Time: O(1); Space: O(1)
# count of the trial : k, k-1, k-2, k-3, ......,1
# n >= k(k + 1)/2
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return int ( ( -1 + sqrt( 8*n + 1 ) - 0.0001) // 2 + 1 )