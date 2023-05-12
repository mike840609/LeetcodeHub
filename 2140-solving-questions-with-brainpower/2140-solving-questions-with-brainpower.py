class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            x, y = questions[i]
            
            if i + y + 1 >= n:
                dp[i] = x
                if i+1 < n:
                    dp[i] = max(dp[i], dp[i+1])
            else:
                dp[i] = max(x+dp[i+y+1], dp[i+1])
        
        return dp[0]