class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dp = [0] * 26
        
        for c in sentence:
            idx = ord(c)-ord('a')
            dp[idx] = 1
            
        return all(dp)
            