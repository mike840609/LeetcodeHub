class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        A = list(accumulate([0] + nums))
        res = 0 
        s = defaultdict(list)
        
        for i in range(len(A)):
            s[A[i]].append(i)
            
            
        for i in range(len(A)):
            if k+A[i] in s:
                idx = bisect_right(s[k+A[i]], i)
                res += len(s[k+A[i]]) - idx
                
        return res