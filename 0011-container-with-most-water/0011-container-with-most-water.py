class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        result=0
        while i<j:
            width=j-i
            length=min(height[i],height[j])
            area=length*width
            if result<area:
                result=area
            if   height[i]>height[j]:
                j-=1
            else:
                i+=1
        return result
            