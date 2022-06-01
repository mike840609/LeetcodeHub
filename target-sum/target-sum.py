class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cnt = {0:1}
        for i in nums:            
            tmpCnt = defaultdict(int)
            for x in cnt:
                tmpCnt[x+i] += cnt[x]
                tmpCnt[x-i] += cnt[x]
            cnt = tmpCnt
                                
        return cnt.get(target, 0)            
            
        