class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dp = [0] * (len(num1) + len(num2)) 
        
        num1 = list(map(int, num1[::-1]))
        num2 = list(map(int, num2[::-1]))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                dp[i+j] += num1[i] * num2[j]
        
        carry = 0 
        for i in range(len(dp)):
            dp[i] += carry
            carry = dp[i] // 10 
            dp[i] %= 10 
                
        return str(int(''.join([str(x) for x in dp[::-1]])))
            
                
                