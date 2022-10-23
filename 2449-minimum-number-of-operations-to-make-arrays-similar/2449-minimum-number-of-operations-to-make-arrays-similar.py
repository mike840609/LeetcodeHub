class Solution:
    def makeSimilar(self, A: List[int], B: List[int]) -> int:
        A1 = sorted(a for a in A if a % 2)
        A2 = sorted(a for a in A if a % 2 == 0)
        B1 = sorted(a for a in B if a % 2)
        B2 = sorted(a for a in B if a % 2 == 0)
        
        res1 = sum(abs(a-b)//2 for a, b in zip(A1, B1))
        res2 = sum(abs(a-b)//2 for a, b in zip(A2, B2))
    
        return (res1 + res2) // 2