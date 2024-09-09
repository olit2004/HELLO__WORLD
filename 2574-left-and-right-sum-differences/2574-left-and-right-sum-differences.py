class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in range(len(nums)):
            left_sum=0
            right_sum=0
            for j in range(len(nums)):
                if j<i:
                    left_sum+=nums[j]
                elif j>i:
                    right_sum+=nums[j]
            if left_sum>right_sum:
                answer.append(left_sum - right_sum)
            else :
                answer.append(right_sum - left_sum)
        return answer        