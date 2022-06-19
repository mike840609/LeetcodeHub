class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {} 
        for product in products:
            p = trie            
            for c in product:
                p.setdefault(c, {})
                p.setdefault('result', [])
                p['result'].append(product)
                p = p[c]
            
            p.setdefault('result', [])
            p['result'].append(product)
            
        
        res = [] 
        p = trie
        # print(p)
        for c in searchWord:
            res.append(sorted(p.get(c, {}).get('result', []))[:3])
            p = p.get(c, {})
            
        return res
                