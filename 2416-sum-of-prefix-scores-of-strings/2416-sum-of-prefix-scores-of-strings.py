class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = {}
        
        for word in words:
            p = trie
            for w in word:                
                if w in p :
                    p[w]['#'] += 1                                        
                else:
                    p[w] = {'#':1}
                p = p[w]            
                
            
        res = []
        for word in words:
            p = trie            
            tmp = 0
            for w in word:
                if w in p:
                    p = p[w]
                    tmp += p['#']
                else:
                    break                   
            
            res.append(tmp)
            
        return res
                
                    
                    
                            
            