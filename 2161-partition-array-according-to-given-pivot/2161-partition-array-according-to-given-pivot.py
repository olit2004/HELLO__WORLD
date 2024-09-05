class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less=[]
        equal=[]
        greater=[]
        for i in nums :
            if i == pivot:
                equal.append(i)
            elif i>pivot:
                greater.append(i)
            else :
                less.append (i)
        return less+equal+greater                