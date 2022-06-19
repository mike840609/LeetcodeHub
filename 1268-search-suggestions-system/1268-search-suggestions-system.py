class Solution:
    def suggestedProducts(self, A: List[str], word: str) -> List[List[str]]:
        A.sort()
        res, prefix = [], ''
        for c in word:
            prefix += c 
            i = bisect.bisect_left(A, prefix)
            res.append([w for w in A[i:i+3] if w.startswith(prefix)])
        return res 
                