# Example : [6, 2, 3, 4]
# 1. [6]
# 2. [6, 2]
# 3. [6, 2] 3; pull 2 to pair leafs and push 3 into stack
 
   6
  / \
 2   3   
# 4. [6, 3]
# 5. [6, 3] 4; pull 3 to pairs leafs and push 4 into stack
   
       12
      /  \ 
     6    4
    / \
   2   3  
# 6. [6, 4]

      24
     /  \
    6    12 
        /  \
       6    4
      / \
     2   3

#Time: O(N)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res, stack = 0, [float('inf')]

        for a in arr:
            while ( a >= stack[-1] ):
                mid = stack.pop()
                res += mid * min( stack[-1], a )
            stack.append(a)
        while ( len( stack ) > 2 ):
            res += stack.pop() * stack[-1]
        return res