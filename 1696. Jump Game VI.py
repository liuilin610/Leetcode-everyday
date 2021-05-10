#Time: O(N)
class Solution:
    def maxResult(self, nums: List[int], k:int) -> int:
        n = len(nums)
        res = [0]* n
        res[0] = nums[0]
        dq = deque()
        # use dq to store the index and select the maxSum
        dq.append(0)

        for i in range(1, n):
            # remove the smaller index in a jump step ( len = k )
            while (dq) and ( dq[0] < i - k):
                dq.popleft()
            res[i] = res[dq[0]] + nums[i]
            #remove the smaller value 
            while (dq) and (res[i] >= res[dq[-1]]):
                dq.pop()
            dq.append(i)
        return res[-1]