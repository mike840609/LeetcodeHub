class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        
        s = list(self.countAndSay(n-1))
        # print(s)
        tmp = ''        
        q = []
        
        while s:
            while not q or (s and q[-1] == s[0]):
                q.append(s.pop(0))
            
            tmp += str(int(len(q))) + q[0]
            q = []
        
        if q :            
            tmp = len(q) * q[0] + tmp
                
        return tmp        
            
                
                