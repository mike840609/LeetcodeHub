class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        
        s = set()
        res = 0
        for k,v in cnt.items():
            if v not in s:
                s.add(v)
            else:
                for j in range(0, v+1):
                    if v - j not in s or v-j == 0:
                        s.add(v-j)
                        res += j
                        break
        return res
            