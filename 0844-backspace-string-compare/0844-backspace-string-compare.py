class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl=[]
        for i in s:
            if  i!="#":
                sl.append(i)
            elif sl:
                sl.pop()
        tl=[] 
        for i in t:
            if  i!="#":
                tl.append(i)
            elif tl:
                tl.pop()  
        return sl==tl        
            