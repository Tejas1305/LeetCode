class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        bitwise_or = 0
        max_len = 0
        
        for right in range(len(nums)):
            while (bitwise_or & nums[right]) != 0:
                bitwise_or ^= nums[left]  # Remove nums[left] from the window
                left += 1

            bitwise_or |= nums[right]  # Add nums[right] to the window
            max_len = max(max_len, right - left + 1)

        return max_len