class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num  # Calculate the maximum possible OR value

        count = 0
        n = len(nums)

        # Function to calculate bitwise OR for a subset
        def subset_or(subset):
            or_value = 0
            for num in subset:
                or_value |= num
            return or_value

        # Generate all non-empty subsets and count the ones that match the max OR value
        for i in range(1, 1 << n):  # Iterate over all subsets
            subset = [nums[j] for j in range(n) if (i & (1 << j)) > 0]
            if subset_or(subset) == max_or:
                count += 1

        return count
