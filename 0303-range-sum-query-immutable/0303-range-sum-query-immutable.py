class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        cnt=0
        while left <= right:
            if left ==right:
                 cnt+= self.nums[left]
            else  :      
                cnt+= self.nums[left]+self.nums[right]
            left+=1
            right-=1
        return cnt    
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)