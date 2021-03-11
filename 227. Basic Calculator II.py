class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s + '+0'# calculate all the num until the last one
        num = 0
        sign = '+'
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
                #print (c, stack)
            if c in '+-*/':
                if sign == '+':
                    stack.append(num)
                    #print (c,stack,"A")
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                    
                elif sign == '/':
                    tmp = stack[-1]
                    if tmp >= 0:
                        #print (c, stack,'b')
                        stack.append( stack.pop()// num)
                        #print (c, stack,'B')
                    if tmp < 0:
                        stack.append ( - (abs(stack.pop())//num))
                num = 0
                sign = c
        return sum(stack)