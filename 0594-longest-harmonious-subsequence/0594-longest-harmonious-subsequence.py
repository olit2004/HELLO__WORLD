class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_dict={}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] +=1
            else :
                freq_dict [i]=1
         
        max_length =0
        for i in freq_dict :
            if i+1 in freq_dict :
                if max_length < freq_dict[i]+freq_dict[i+1]:
                     max_length=freq_dict[i]+freq_dict[i+1]
        return max_length            
            
        