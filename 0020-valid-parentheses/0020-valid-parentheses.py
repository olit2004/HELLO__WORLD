class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts={'(':')','[':']','{':'}'}
        stk=[]
       
        
        for i in s:
            if len(stk)==0 and i  in dicts.keys()  :
                stk.append(i)
            elif len(stk)==0 and i  in dicts.values()  :
                return False
            else:
                chk=stk.pop()
                if i in dicts.keys() :
                    stk.append(chk)
                    stk.append(i)
                elif i==dicts[chk]  :
                    continue
                else :
                    return False
        if  len (stk) ==0:
            return True
        else:
            return False