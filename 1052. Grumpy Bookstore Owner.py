class Solution:
    def maxStisfied(self, customers: List[int], grumpy: List[int], x: int) -> int
    # The function to find the maximum satisfied customers.
    # Sum all the customers with not grumpy owner
    # slide window of the sum of grumpy customers and find the maximum!
    
    n = len(customers)
    # if the time period is less than the secret time, all customers are satified.
    if n <= X: return sum(customers)

    # Sum of all satisfied customers
    Sum = 0
    for i in range(n):
        if grumpy[i] == 0:
            Sum += customers[i]
            customers[i] = 0

    # the maximum slide window of customers changes their mind
    tmp = 0
    for i in range(X):
        tmp += customers[i]
    MaxWindow = tmp
    for i in range(X, n):
        tmp = tmp + customers[i] -customers[i - X]
        MaxWindow = max(MaxWindow, tmp)
    
    return Sum + MaxWindow