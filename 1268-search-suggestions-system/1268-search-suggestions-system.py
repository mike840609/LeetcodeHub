class Solution:
    def suggestedProducts(self, A: List[str], word: str) -> List[List[str]]:
        A.sort()
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c 
            # usd lo for better performance, bisect_left(a, x, lo=0, hi=len(a), *, key=None)
            i = bisect.bisect_left(A, prefix, i)
            res.append([w for w in A[i:i+3] if w.startswith(prefix)])
        return res 
                