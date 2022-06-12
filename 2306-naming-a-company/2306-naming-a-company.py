class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        for idea in ideas:
            d[idea[0]].add(idea[1:])
        
        res = 0
        for a, setA in d.items():
            for b, setB in d.items():
                if a >= b :
                    continue
                
                same = setA & setB
                
                res += len(setA - same) * len(setB - same)
                
        return res * 2 
            
                