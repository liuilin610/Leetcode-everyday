#Time : O(N); Space: O(1)
# use prefix sum idead to record the states of [a,e,i,o,u]
# two choice for each(even, odd); therefore, 11111(5 bits idea)
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a' : 1, 'e' : 2, 'i' : 4, 'o' : 8, 'u' : 16}
        # preset 0 for 00000, all even for aeiou
        res, prefix, state = 0, 0, {0: -1}
        for i, c in enumerate(c):
            if c in vowels:
                prefix ^= vowels[c]
            if prefix not in state:
                state[prefix] = i
            #if the prefix in state: even aeiou subarray 
            #if not vowels, i would still increase
            else:
                res = max(res, i - state[prefix] )
        return res

        