class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2 
        diff = [] 
        n = len(nums1)
        
        for x, y in zip(nums1, nums2):            
            diff.append(abs(x-y))            
        M = max(diff)
        bucket = [0] * (M + 1)
        for i in range(n):
            bucket[diff[i]] += 1
        
        for i in range(M, 0, -1):
            if bucket[i] > 0 :
                minus = min(bucket[i], k)
                bucket[i] -= minus
                bucket[i-1] += minus
                k -= minus
        
        return sum([i*i*bucket[i] for i in range(M, 0, -1)])
        