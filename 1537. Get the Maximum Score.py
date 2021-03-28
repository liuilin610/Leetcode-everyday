class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, n1, n2 = 0, 0, len(nums1), len(nums2)
        route1, route2 = 0, 0
        while ( i < n1 ) or ( j < n2 ):
            if ( i < n1 ) and ( ( j == n2 ) or ( nums1[i] < nums2[j] ) ):
                route1 += nums1[i]
                i += 1
            elif ( j < n2 ) and ( ( i == n1 ) or ( nums1[i] > nums2[j] ) ):
                route2 += nums2[j]
                j += 1
            else:
                route1 = route2 = max( route1, route2) + nums1[i]
                i += 1
                j += 1
        return ( max( route1, route2 ) % (10 ** 9 + 7 ))