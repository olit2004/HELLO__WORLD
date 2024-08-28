class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def remover (st):
            stk=[]
            for i in st:
                if  i!="#":
                    stk.append(i)
                elif stk:
                    stk.pop()
            return stk
        sl=remover(s)
        tl= remover(t)
        return  sl==tl
        
            
            