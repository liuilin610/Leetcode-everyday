class Solution:
    def search(self, nums: List[int], target: int) _> int:
        # binary search clear
        n = len(nums)
        def bisearch ( arr, i, f, key):
            L, R = i, f
            while ( L < R):
                mid = ( L + R) // 2
                if key ( arr[mid]): L = mid + 1
                else: R = mid
            return L
        
        pivot = bisearch( nums, 0, n - 1, key = lambda x: x > nums[-1])
        a = bisearch( nums, pivot, n - 1, key = lambda x: x < target)
        b = bisearch (nums, 0, pivot -1, key = lambda x : x < target)

        for x in (a, b):
            if ( x < 0) or ( x >= n): continue
            if (nums[x] == target) : return x
        return -1
            


        # I. Time complexity : O (N)
        n = len(nums)
        for i in range(n):
            if nums[i] == target: return i
        return -1
        
        ## binar search
        n = len(nums)
        L, R = 0, n - 1
        while ( L < R):
            mid = ( L + R) // 2
            if ( nums[mid] == target): return mid
            elif (nums[L] < nums[mid]:)
                if ( nums[L] <= target < nums[mid]):
                    R = mid
                else:
                    L = mid + 1
            else:
                if (nums[mid + 1] <= target <= nums[R]):
                    L = mid + 1
                else:
                    R = mid
            return (L if ( nums[L] == target) else -1 )
