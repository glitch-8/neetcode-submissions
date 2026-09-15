class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        idx = 0
        output = list()
        while idx<len(nums) - 2:
            left = idx + 1
            right = len(nums) - 1
            while left<right:
                if nums[left] + nums[idx] + nums[right] == 0:
                    output.append((nums[left], nums[idx], nums[right]))

                    while left<right and (nums[left] == nums[left + 1]):
                        left += 1
                    
                    while right>left and (nums[right] == nums[right - 1]):
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif nums[left] + nums[idx] + nums[right] < 0:
                    left += 1 
                else:
                    right -= 1
            
            while idx<len(nums) - 2 and nums[idx] == nums[idx + 1]:
                idx += 1
            
            idx += 1

        return output




