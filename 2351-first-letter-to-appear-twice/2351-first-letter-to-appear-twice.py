class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        already=[]
        for i in s:
            if i in already:
                return i
            else :
                already.append(i)