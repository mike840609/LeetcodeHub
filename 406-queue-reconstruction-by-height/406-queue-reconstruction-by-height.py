'''
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
---------------------------------
[[7, 0]]
[[7, 0], [7, 1]]
[[7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the people from tall to short
        # insert from tall to short (insert at index = p[1])
        people.sort(key=lambda p: (-p[0], p[1]))
        # print(people)
        # print('---------------------------------')
        res = []
        for p in people:
            res.insert(p[1], p)
            # print(res)
        return res