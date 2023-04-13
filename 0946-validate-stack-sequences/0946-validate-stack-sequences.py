class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        pushed = deque(pushed)
        for x in popped:
            if stk and stk[-1] == x:
                stk.pop()
                
            else:
                while pushed:                    
                    stk.append(pushed.popleft())
                    
                    if stk[-1] == x:
                        stk.pop()
                        break
                        
        return len(stk) == 0
                
                
            