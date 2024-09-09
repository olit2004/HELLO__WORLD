class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        freq_s=[0]*26
        freq_t=[0]*26
        for i in s:
            freq_s[ord(i)-ord("a")]+=1
            
        for j in t:   
            freq_t[ord(j)-ord("a")]+=1
        cnt=0
        for i in range (26):
            if  freq_s[i]>freq_t[i]:
                cnt+= freq_s[i]-freq_t[i]
        
        return   cnt   
                