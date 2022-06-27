class Solution:
    def minPartitions(self, n: str) -> int:
        res = [int(x) for x in n]        
        return max(res)