class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rsum=[]
       
        sm=0
        for i in range (len(nums)):
            
            sm+=nums[i]
            rsum.append(sm)   
                
        return rsum   