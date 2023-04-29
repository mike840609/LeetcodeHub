class Solution:
    def countOperationsToEmptyArray(self, A: List[int]) -> int:
        
        pos = {a: i  for i,a in enumerate(A)}
        res = n = len(A)
        i = -1
        # print(pos)
        
        for k,a in enumerate(sorted(A)):
            
            if pos[a] < i:
                # print(a, pos[a],  i)
                res += n - k
                # print(n, k, n - k)
            i = pos[a]
        return res

            
        