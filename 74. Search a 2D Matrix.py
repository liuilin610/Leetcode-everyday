class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) - bool:

        # binary search 
        # Time Complexity: O(log(m*n))
        m, n, = len(marix), len(matrix[0])
        if ( target > matrix[-1][-1] ) or ( target < matrix[0][0] ): return False

        L, R = 0, m* n - 1
        while ( L <= R ):
            mid = ( L + R ) // 2
            if ( matrix[mid // n][mid % n] == target ): return True
            elif (matrix[mid // n][mid % n] > target ):
                R = mid - 1
            else:
                L = mid + 1
        return False
        

        # Time Complexity: O(m+n)
        m, n = len(matrix), len(matrix[0])
        # target is smaller than the smallestt or larger than maximum
        if ( target > matrix[-1][-1] ) or ( target < matrix[0][0] ): return False
        # find the related row
        for i in range( m - 1 ):
            if ( matrix[i][0] <= target ) and ( target < matrix[i+1] ):
                kk = i
            elif (target >= matrix[-1][0]):
                kk = m - 1
        
        for j in range(n):
            if ( matrix[kk][j] == target ):
                return True
            elif ( matrix[kk][j] > target ):
                return False
        # if target is larger than the final element in the row
        return False 