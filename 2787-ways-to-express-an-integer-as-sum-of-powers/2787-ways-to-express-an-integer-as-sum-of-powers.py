class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp, k = [1] + [0] * n, 1
        for i in range(1, n + 1):
            power = i ** x
            for j in range(n, power - 1, -1):
                dp[j] += dp[j - power]
                dp[j] %= 10 ** 9 + 7
        return dp[n]
        