class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = len(nums) - 1
        min_idx = None
        while left<right:
            mid = (left + right)//2

            if nums[left]<nums[mid] and nums[mid]<nums[right]:
                min_idx = left
                break
            
            if left == mid:
                min_idx = left if nums[left]<nums[right] else right
                break

            if nums[left]>nums[mid]:
                right = mid
            elif nums[right]<nums[mid]:
                left = mid
        
        if min_idx is None:
            min_idx = mid

        def binary_search(target, arr):
            left = 0
            right = len(arr) - 1
            while left<=right:
                mid = (left + right)//2
                if target == arr[mid]:
                    return mid
                elif target>arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        print(min_idx)
        if min_idx == 0:
            print(binary_search(target, nums))
            return binary_search(target, nums)

        # if target>nums[0] and target<nums[min_idx-1]:
        if target>nums[-1]:
            return binary_search(target, nums[:min_idx])
        
        else:
            idx = binary_search(target, nums[min_idx:])
            if idx == -1:
                return idx
            return idx + min_idx


