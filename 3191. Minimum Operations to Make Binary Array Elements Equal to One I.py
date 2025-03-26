class Solution(object):
    def minOperations(self, nums):
        ans = 0

        for index, value in enumerate(nums):
            if value == 0:
                if index + 2 >= len(nums):
                    return -1
                
                nums[index + 1] ^= 1
                nums[index + 2] ^= 1
                ans += 1
        
        return ans