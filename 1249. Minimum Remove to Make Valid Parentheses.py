class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res, stack, tmp = [], [], 0

        for i in s:
            res.append(i)
            if ( i == '(' ):
                tmp += 1
                stack.append(len(res) -1 )
            elif ( i == ')' ):
                tmp -= 1
            if ( tmp < 0 ):
                tmp += 1
                stack.pop()
        while ( tmp > 0 ):
            tmp -= 1
            res.pop(stack[-1])
            stack.pop()
        return ''.join(res)
        

            