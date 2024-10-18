class Solution:
    def countMaxOrSubsets(self, A):
        dp = collections.Counter([0])
        for a in A:
            for k, v in list(dp.items()):
                dp[k | a] += v
        return dp[max(dp)]
