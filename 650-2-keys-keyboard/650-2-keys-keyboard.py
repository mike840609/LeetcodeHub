class Solution:
    def minSteps(self, n: int) -> int:        
        if n == 1: return 0
        dp = [0] * (n+1) 
        dp[0] = 1
        prev = 1 
        
        for i in range(1, n+1):
            for j in range(i-1, 0, -1):
                # if sequence of length 'j' can be pasted multiple times to get length 'i' sequence
                if i%j == 0:
                    # we just need to paste sequence j (i/j - 1) times, hence additional (i/j) times since we need to copy it first as well.
                    # we don't need checking any smaller length sequences
                    # here: actually should be +1(copy) -1(original part)
                    dp[i] = dp[j] + i//j
                    break
                    
        return dp[-1]
            