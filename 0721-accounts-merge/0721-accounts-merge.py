class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        p = {}        
        
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        
        def union(i, j):
            p[find(i)] = find(j)
            
        for acc in accounts:                    
            name = acc[0]                 
            
            for mail in acc[1:]:
                if mail not in p:
                    p[mail] = mail
                
                d[mail] = name
                union(mail, acc[1]) 
        
        trees = defaultdict(list)
        for mail in p.keys():
            trees[find(mail)].append(mail)
        
        return [[d[root]] + sorted(mails) for root, mails in trees.items()]
            