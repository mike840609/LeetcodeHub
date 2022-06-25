class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        A1, A2 = nums[::], nums[::]
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                A1[i] = nums[i+1]
                A2[i+1] = nums[i]
                break
        
        return A1 == sorted(A1) or A2 == sorted(A2)
            