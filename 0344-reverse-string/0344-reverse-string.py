class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n= len (s)-1 
        for i in range(len(s)//2) :
                s[i],s[n]=s[n],s[i]
                n-=1