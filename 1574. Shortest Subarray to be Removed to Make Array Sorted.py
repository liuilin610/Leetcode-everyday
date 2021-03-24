class Solution:
    def ShortestSubarray(self, arr: List[int]) -> int:
        '''
    # for non-decreasing array: arr[i] >= arr[j], i > j
     The subarray could be 1. begins from the left end arr[0]
                           2. ends at the right end arr[-1]
                           3. removes the middle part; the left side connnects with right side 
        '''
    n = len(arr)
    if n < 2: return 0

    #find the Maximum of left end
    L = -1
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            L = i+ 1
            break
    if L = -1: return 0

    #find the minimum of right end
    H = n-1
    for i in range(n-1, -1, -1):
        if arr[i] < arr[i-1]:
            H = i
            break
    MinRemove = min( n- L, H)

    # find the minimum length of removed subarray
    for i in range(L-1, -1, -1):
        for j in range(H, n):
            if arr[i] <= arr[j]:
                MinRemove = min (MinRemove, j - i - 1)
                break
    return MinRemove

                          