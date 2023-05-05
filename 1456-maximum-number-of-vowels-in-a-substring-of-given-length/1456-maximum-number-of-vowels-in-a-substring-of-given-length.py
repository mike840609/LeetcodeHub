class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        w = Counter()
        res = 0
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        tmp = 0 
        for idx, c in enumerate(s):
            
            if idx - k >= 0 and s[idx-k] in vowel:
                tmp -= 1
                
            if c in vowel:
                tmp += 1
                res = max(res, tmp)
            
            
            
        return res
        
        