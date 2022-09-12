class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0 
        tokens = sorted(tokens)
        tokens = deque(tokens)
        ans = score
        
        while tokens and power > 0 :
            while tokens and power >= tokens[0]:
                cost = tokens.popleft()
                power -= cost
                score += 1
            
            ans = max(ans, score)
            
            if tokens and power <= tokens[0] and score > 0:
                score -= 1
                p = tokens.pop()
                power += p
            else:
                break
        
        return ans
                
            
                