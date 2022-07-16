'''
init state
1. hold = float('-inf')[can not start from this state]
2. not_hold = 0, [can start from this state]
3. not_hold_cooldown = float('-inf')[can not start from this state]

state machine:
1. hold -----do nothing----->hold
2. hold -----sell----->notHold_cooldown
3. notHold -----do nothing -----> notHold
4. notHold -----buy-----> hold
5. notHold_cooldown -----do nothing----->notHold
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, not_hold, not_hold_cooldown = float('-inf'), 0, float('-inf')
        
        for p in prices: 
            hold, not_hold, not_hold_cooldown = max(hold, not_hold - p), max(not_hold, not_hold_cooldown), hold + p 
        
        return max(not_hold, not_hold_cooldown)
        