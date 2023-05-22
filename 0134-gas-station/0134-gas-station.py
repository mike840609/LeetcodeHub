class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        
        res = 0
        tmp = 0 
        for i in range(len(gas)):
            tmp += gas[i] - cost[i]
            if tmp < 0 :
                res = i+1
                tmp = 0
        
        return res
                
            