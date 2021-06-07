# Time (O(n log(R)))
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if ( hour <= len(dist) - 1): return -1

        def time(nums, speed):
            n = len(nums)
            res = 0
            for i in range(n - 1):
                res += (nums[i] - 1)// speed + 1
            return res + nums[-1]/speed

        L = max(sum(dist)//hour, 1)
        R = max(dist)/(hour % 1) + 1 if (hour % 1) else max(dist)

        while ( L < R ):
            mid = ( L + R ) // 2
            if ( time(dist, mid) > hour ):
                L = mid + 1
            else:
                R = mid
        return R