class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        total_zeros = 0
        for num in nums:
            if num != 0:
                full_product *= num
            else:
                total_zeros += 1
        
        if total_zeros>1:
            return [0]*len(nums)

        output = list() 
        for num in nums:
            if total_zeros == 1:
                if num == 0:
                    output.append(int(full_product))
                else:
                    output.append(0)
            else:
                output.append(int(full_product/num))

        return output