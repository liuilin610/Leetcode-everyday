# Time:O(1)
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        res = 1
        while self.stack and ( price >= self.stack[-1][0] ):
            res += self.stack.pop()[1]
        self.stack.append([ price, res] )
        return res