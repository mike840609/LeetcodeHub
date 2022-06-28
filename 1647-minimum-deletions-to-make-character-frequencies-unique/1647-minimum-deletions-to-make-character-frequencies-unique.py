class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)            
        res = 0
        seen = set()
        
        for _, freq in cnt.items():
            while freq in seen and freq > 0:
                freq -= 1
                res += 1                            
            seen.add(freq)
            
        return res
            