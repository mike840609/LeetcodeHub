class TreeNode:
    def __init__(self, start, end, sum, left= None, right=None):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = left
        self.right = right

class NumArray:

    def __init__(self, nums: List[int]):
        
        def build(start, end, vals):
            if start > end:
                return None

            if start == end:
                return TreeNode(start, end, vals[start])

            m = (start + end) // 2
            left = build(start, m, vals)
            right = build(m+1, end, vals)
            return TreeNode(start, end, left.sum + right.sum, left, right)
            
        self.root = build(0, len(nums)-1, nums)
    

    def update(self, index: int, val: int) -> None:
        def update_(root, index, val):
            if root.start == root.end == index:
                root.sum = val 
                return val
            m = (root.start + root.end) // 2
            if index <= m:
                update_(root.left, index, val)
            else:
                update_(root.right, index, val)

            root.sum = root.left.sum + root.right.sum

        return update_(self.root, index, val)


    def sumRange(self, i, j) -> int:
        def sumRange_(root, i, j):
            if root.start == i and root.end == j:
                return root.sum
            
            mid = (root.start + root.end) // 2
            
            if j <= mid:
                return sumRange_(root.left, i, j)

            elif i >= mid + 1:
                return sumRange_(root.right, i, j)

            else:
                return sumRange_(root.left, i, mid) + sumRange_(root.right, mid+1, j)

        return sumRange_(self.root, i, j)





# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)