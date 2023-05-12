class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = [0] * (n+1)
        
        for i in range(n-1, -1, -1):
            x, y = questions[i]                        
            dp[i] = max(x+dp[min(i+y+1, n)], dp[i+1])
        
        return dp[0]