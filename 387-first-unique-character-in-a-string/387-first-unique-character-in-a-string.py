class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        cnt = Counter()
        for i, c in enumerate(s):            
            d[c] = i
            cnt[c] += 1
        
        for i, c in enumerate(s):
            if d[c] == i and cnt[c] == 1:
                return i
        return -1
            
        
        
            