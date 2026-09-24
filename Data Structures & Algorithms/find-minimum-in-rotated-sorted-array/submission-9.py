class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        while left<right:
            print(left, right)
            mid = (left + right)//2

            if nums[left]<nums[mid] and nums[mid]<nums[right]:
                return nums[left]
            
            if left == mid:
                return min(nums[left], nums[right])

            if nums[left]>nums[mid]:
                right = mid
            elif nums[right]<nums[mid]:
                left = mid
            
        return nums[mid]