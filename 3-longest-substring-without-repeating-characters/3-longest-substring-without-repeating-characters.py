class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = -1
        d = {}
        res = 0
        for idx, c in enumerate(s):
            if c not in d or d[c] < i:
                res = max(idx-i, res)
            else:
                i = d[c]
                
            d[c] = idx
            
        return res
                