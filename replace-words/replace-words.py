class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        
        self.d = {}
        
        for word in dictionary:
            p = self.d
            for c in word:
                if c not in p:
                    p[c] = {}
                
                p = p[c]
                
            p['#'] = True 
        
        def getReplace(word):
            p = self.d
            res = ''
            
            for w in word:             
                
                if '#' in p:
                    return res
                
                res += w
                
                if w not in p:
                    return word
                
                p = p[w]
                
            return res 
        
        # print(self.d)
        l = [getReplace(x) for x in sentence.split()]
        return ' '.join(l)
        
                
        
        