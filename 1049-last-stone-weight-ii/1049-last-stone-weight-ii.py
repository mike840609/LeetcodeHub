class Solution:
    def lastStoneWeightII(self, A):
        dp = {0}
        for a in A:
            dp = { x+a for x in dp} | {abs(x-a) for x in dp}
        return min(dp)
        