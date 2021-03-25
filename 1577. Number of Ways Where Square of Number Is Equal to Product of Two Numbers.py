class Solution:
    def tripletnum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = 0
        dic1 = {}
        dic2 = {}
        for i in range(n1):
            for k in range(i + 1, n1):
                dic1[ nums1[i]* nums1[k]] = dic1.get(nums1[i] * nums1[k], 0) +1
        for j in range(n2):
            for k in range(j + 1, n2):
                dic2[nums2[j] * nums2[k]] = dic2.get(nums2[j] * nums2[k], 0) + 1
        for i in range(n1):
            if nums1[i] ** 2 in dic2:
                res += dic2[ nums1[i] ** 2]
        for j in range(n2):
            if nums2[j] ** 2 in dic1:
                res += dic1[ nums2[j] ** 2]
        return res
        '''
        n1, n2 = len(nums1), len(nums2)
        res = 0
        dic1 = collections.Counter([i ** 2 for i in nums1])
        dic2 = collections.Counter([j ** 2 for j in nums2])
        for i in range(n1):
            for k in range(i + 1, n1):
                if (nums1[i] * nums1[k] in dic2):
                    res += dic2[ nums1[i] * nums1[k]]
        for j in range(n2):
            for k in range(j + 1, n2):
                if (nums2[j] * nums2[k] in dic1):
                    res += dic1[ nums1[j] * nums2[k]]
        return res
        '''