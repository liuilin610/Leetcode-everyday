class Solution:
def peakIndex(self, arr: List[int]) -> int:
    n = len(arr)
    L, R = 0, n - 1
    while ( L < R ):
        mid = ( L + R ) // 2
        if ( arr[mid] < arr[mid + 1] ):
            L = mid + 1
        else:
            R = mid
    return L