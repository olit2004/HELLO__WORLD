class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rsum=[]
        for i in range (len(nums)):
            sm=0
            for j in range(i+1):
                sm+=nums[j]
            rsum.append(sm)   
                
        return rsum   