class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals={'I':1,'V':5 ,'X':10,'L':50,'C':100,'D':500,'M':1000}
        x=y=0
        for i in s:
            if numerals [i]>y:
                x-=(2*y)
            y=numerals[i]
            x+=y
        return x    
     
        