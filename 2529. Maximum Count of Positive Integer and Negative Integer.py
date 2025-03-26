class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        countn =0
        for number in nums:
            if number>0:
                count+=1
            elif number<0:
                countn+=1
        
        return(max(count,countn))