class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t=x
        collection=0
        while x>0:
            lastdigit=x%10
            collection= collection*10+lastdigit
            
            x=x//10
            
        if t==collection:
            return True
        else :
            return False    