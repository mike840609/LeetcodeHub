class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        q = []
        for c in s:
            q.append(c)
            if len(q) >= 2:
                if q[0] != q[1]:
                    res += 1
                q = []
        return res
                    
                