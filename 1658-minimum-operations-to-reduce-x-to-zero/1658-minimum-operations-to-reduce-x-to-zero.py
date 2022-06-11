class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        rSum = [0] + list(accumulate(nums))
        lSum = list(accumulate(nums[::-1]))[::-1] + [0]
        
        
        res = sys.maxsize
        
        d = {}
        for i, val in enumerate(rSum):
            d[val] = i
        
        
        for i in range(len(lSum)-1, -1, -1):
            val = lSum[i]
            
            if x-val in d:
                idx = d[x-val]
                if idx <= i:
                    res = min(res, len(nums) - (i - idx))

        return res if res != sys.maxsize else -1