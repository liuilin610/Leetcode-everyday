class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        #stack
        preorder = preorder.split(',')
        stack =[]
        for c in preorder:
            stack.append(c)

        while len(stack) >= 3 and (stack[-1] == stack[-2] ='#') and stack[-3]!= '#':
            stack.pop(), stack.pop(),stack.pop()
            stack.append('#')
        return stack == ['#']

        #in and out of node in tree
        nodes = preorder.split(',')
        # all nodes would have two out(+1) one in(-1), leaf has one in (-1) and root has one in and two out.
        diff = 1
        for node in node:
            diff -= 1
            if diff <0: return False
            if node != '#':
                diff += 2
        return diff == 0