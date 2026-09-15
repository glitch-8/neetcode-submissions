class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        if len(nums) == 1:
            return 1

        nums.sort()
        left = 0
        right = 1
        max_range_size = 1
        while right<len(nums):
            if nums[left] + 1 == nums[right]:
                while right<len(nums) and (nums[right - 1] + 1 == nums[right]):
                    right += 1
                
                max_range_size = max(max_range_size, right - left)
            
            left = right
            right += 1
        
        return max_range_size

                





                
        